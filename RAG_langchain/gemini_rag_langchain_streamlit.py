import os
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
import streamlit as st

GOOGLE_API_KEY= "************"
LANGCHAIN_API_KEY = "************"
LANGCHAIN_PROJECT = "************"

pdfs = [r'D:\RAG_langchain\New folder\Account Statement.pdf']


st.title("RAG with Gemini model: gemini-1.5-pro")

loader = PyMuPDFLoader(file_path=pdfs[0]) # entire pdf loaded in single doc
data = loader.load() # load documnets


splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = splitter.split_documents(data)


# import google.generativeai as genai
# genai.configure(api_key=GOOGLE_API_KEY)

# Set your Google API key
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY


# Initialize the embeddings and LLM model
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.3, max_tokens=500)


if os.path.exists(r"D:\RAG_langchain\vectorstore_" + pdfs[0].split("\\")[-1].replace(".pdf","")):
    pass
else:
    os.makedirs(r"D:\RAG_langchain\vectorstore_" + pdfs[0].split("\\")[-1].replace(".pdf",""))

persist_directory = r"D:\RAG_langchain\vectorstore_" + pdfs[0].split("\\")[-1].replace(".pdf","")

# Create the vector store
vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory= persist_directory)

# Initialize retriever
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 6})


system_prompt = (
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer "
    "the question. If you don't know the answer, say that you "
    "don't know. Use three sentences maximum and keep the "
    "answer concise."
    "\n\n"
    "{context}"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the chat interface
if len(st.session_state.messages)>0:
    for message in st.session_state.messages:
        if 'human' in  message.keys():
            with st.chat_message('human'):
                st.write(message["human"])
        if 'system' in  message.keys():
            with st.chat_message('system'):
                st.write(message["system"])

question = st.chat_input("Ask a question")
if question:
    response = rag_chain.invoke({"input": question})
    try:
        with st.chat_message('human'):
            st.write(question)
        with st.chat_message('system'):
            st.write(response["answer"])
    except:
        pass
    st.session_state.messages.append({"human": question, "system": response["answer"]})

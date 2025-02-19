
from langchain_community.document_loaders import PyMuPDFLoader

GOOGLE_API_KEY= "AIzaSyDMdPhM5dj5OG95kfF2hsSUq4j1w7IXz9k"
LANGCHAIN_API_KEY = "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"
LANGCHAIN_PROJECT = "playground"


pdfs = [r'D:\ALM\Vincent\Archive (1)/25NNCV00617.pdf']

loader = PyMuPDFLoader(file_path=pdfs[0]) # entire pdf loaded in single doc
data = loader.load() # load documnets

len(data)
print(data)

for i in data:
    print(i.page_content)

from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)

chunks =  splitter.split_documents(data)

print(f"Total number of chunks divided : {len(chunks)}")
print("Total number of chunks divided :", len(chunks))

from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# import google.generativeai as genai
# genai.configure(api_key=GOOGLE_API_KEY)

# Set your Google API key
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

# Initialize the embeddings model
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

vector = embeddings.embed_query("Who is plaintiff?")
print(vector)
len(vector)
##768

vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory=r"D:\RAG_langchain\vectorstore_gemini")

retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 6})

retrieved_docs = retriever.invoke("Who is plaintiff?")

len(retrieved_docs)
6

print(retrieved_docs[5].page_content)

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.3, max_tokens=500)

from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

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

response = rag_chain.invoke({"input": "Who is plaintiff?"})
print(response["answer"])
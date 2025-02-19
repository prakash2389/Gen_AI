import streamlit as st
import time
import os
from langchain_openai import OpenAI
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_community.document_loaders import UnstructuredPDFLoader, PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
load_dotenv()


st.title("RAG Application")

pdfs = [r'D:\ALM\Vincent\Archive (1)/25NNCV00617.pdf']

api_key = "***********************************************************************************************"


# loader = UnstructuredURLLoader(url=pdfs)
# data = loader.load()
#
# loader = UnstructuredPDFLoader(file_path=pdfs[0])
# data = loader.load()

loader = PyMuPDFLoader(file_path=pdfs[0])
data = loader.load()


text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs = text_splitter.split_documents(data)

all_splits = docs
vectorstore = Chroma.from_documents(documents=all_splits, embedding=OpenAIEmbeddings(api_key = api_key),persist_directory=r"D:\RAG_langchain\vectorstore")
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 6})


llm = OpenAI(temperature=0.4, max_tokens=500, api_key = api_key)

query = st.chat_input("Say something: ")
prompt = query

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

if query:
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)

    response = rag_chain.invoke({"input": query})
    #print(response["answer"])

    st.write(response["answer"])

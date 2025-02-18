import streamlit as st
import time
import os
from langchain_openai import OpenAI
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
load_dotenv()

# Set the title of the Streamlit app
st.title("RAG Application")

# List of URLs to load data from
urls = ['https://en.wikipedia.org/wiki/2024_Indian_general_election']

# Placeholder for the API key
api_key = "*************************"

# Load data from the URLs
loader = UnstructuredURLLoader(urls=urls)
data = loader.load()

# Split the loaded data into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000)
docs = text_splitter.split_documents(data)

# Store the document splits in a vector store
all_splits = docs
vectorstore = Chroma.from_documents(documents=all_splits, embedding=OpenAIEmbeddings(api_key = api_key))
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 6})

# Initialize the OpenAI language model
llm = OpenAI(temperature=0.4, max_tokens=500, api_key = api_key)

# Get user input from the Streamlit chat input
query = st.chat_input("Say something: ")
prompt = query

# Define the system prompt for the assistant
system_prompt = (
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer "
    "the question. If you don't know the answer, say that you "
    "don't know. Use three sentences maximum and keep the "
    "answer concise."
    "\n\n"
    "{context}"
)

# Create a chat prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

# If there is a user query, process it
if query:
    # Create a question-answer chain
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)

    # Get the response from the RAG chain
    response = rag_chain.invoke({"input": query})
    
    # Display the response in the Streamlit app
    st.write(response["answer"])

import langchain
import langchain_experimental
import langchain_community
from  langchain_ollama.llms import OllamaLLM
from langchain.prompts import ChatPromptTemplate
import streamlit as st

st.title("Chatbot with LLama3 (Ollama)")

system_template = "you are helpful assistant, answer users question below: {input}"

prompt = ChatPromptTemplate.from_template(system_template)

model = OllamaLLM(model="llama3")

chain = prompt | model


question = st.chat_input("Enter you question?")

if question:
    llama_response = chain.invoke({"input": "What is 45+23?"})
    llama_response

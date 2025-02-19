import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core import Settings
from llama_index.llms.openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def setup_environment():
    """Setup the environment and configurations"""
    # Make sure you have set your OpenAI API key in .env file
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("Please set OPENAI_API_KEY in your environment variables")

def configure_settings():
    """Configure global settings for LlamaIndex"""
    Settings.llm = OpenAI(temperature=0.1, model="gpt-3.5-turbo", api_key = "****************************************************************")
    return Settings

def load_and_index_documents(pdf_directory):
    """Load PDF documents and create an index"""
    # Load documents from the specified directory
    documents = SimpleDirectoryReader(pdf_directory).load_data()

    # Create index from documents
    index = VectorStoreIndex.from_documents(documents)
    return index

def create_query_engine(index):
    """Create a query engine from the index"""
    return index.as_query_engine()



settings = configure_settings()

# Specify your PDF directory
pdf_directory = r"D:\ALM\Vincent\Archive (1)\New folder"

# Create index
index = load_and_index_documents(pdf_directory)

# Create query engine
query_engine = create_query_engine(index)

question = "What is the main topic of the document?"

"""Ask questions and get responses"""
response = query_engine.query(question)
print(response)

print(f"\nQuestion: {response['question']}")
print(f"Answer: {response['response']}\n")



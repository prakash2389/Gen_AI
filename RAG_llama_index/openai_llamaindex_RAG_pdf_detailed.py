
import tiktoken
import openai
import langchain
import llama_index
import pandas as pd
import chromadb
import os


# Import necessary modules from llama_index

from llama_index.core import ServiceContext, PromptHelper, SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.text_splitter import TokenTextSplitter
from llama_index.core.node_parser import MarkdownNodeParser, CodeSplitter, SentenceSplitter
from llama_index.core.node_parser import UnstructuredElementNodeParser


from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.llms.openai import OpenAI
from llama_index.core.settings import Settings
from llama_index.core.node_parser import MarkdownNodeParser, CodeSplitter, SentenceSplitter, UnstructuredElementNodeParser, SemanticSplitterNodeParser, LangchainNodeParser, HierarchicalNodeParser, SimpleNodeParser, SentenceWindowNodeParser, HierarchicalNodeParser

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader


from llama_index.core.postprocessor import MetadataReplacementPostProcessor
from llama_index.core.retrievers import AutoMergingRetriever
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.query_engine import SubQuestionQueryEngine

# Set the OpenAI API key

api_key = "*******************************************************************************************************************************"

# Set the default LLM model
Settings.llm = OpenAI(model="gpt-3.5-turbo",
                      temperature=0.1,
                      api_key = api_key)

# Set the default embedding model
Settings.embed_model = OpenAIEmbedding(
    model="text-embedding-ada-002",
    api_key=api_key)

# Directory containing PDF documents
pdf_directory = r"D:\RAG_langchain\New folder"


# Load documents from the specified directory
documents = SimpleDirectoryReader(pdf_directory).load_data()

# Create index from documents
index = VectorStoreIndex.from_documents(documents)



# Initialize the LLM and embedding model
llm = OpenAI(
    engine="gpt-35-turbo-16k",
    temperature=0.0,
    api_key=api_key
)
embed_model = OpenAIEmbedding(
    model="text-embedding-ada-002",
    api_key=api_key)

# Configure the prompt helper
prompt_helper = PromptHelper(
  context_window=4096,
  num_output=256,
  chunk_overlap_ratio=0.1,
  chunk_size_limit=None
)



def setup_parser():
    # Initialize various node parsers
    simple_node_parser = SimpleNodeParser.from_defaults()
    text_splitter = SentenceSplitter(separator = "\n\n")
    sentence_node_parser = SentenceWindowNodeParser.from_defaults(
        # how many sentences on either side to capture
        window_size=20,
        # the metadata key that holds the window of surrounding sentences
        window_metadata_key="window",
        # the metadata key that holds the original sentence
        original_text_metadata_key="original_sentence",
    )
    ## This node parser will chunk nodes into hierarchical nodes.
    ## Relation-Based Node Parsers
    hierarchical_node_parser = HierarchicalNodeParser.from_defaults(
        chunk_sizes=[4096, 2048, 1024, 512, 256]
    )
    semantic_splitter_node_parser = SemanticSplitterNodeParser(
        buffer_size=5, breakpoint_percentile_threshold=95, embed_model=embed_model
    )
    return simple_node_parser, sentence_node_parser, hierarchical_node_parser, semantic_splitter_node_parser


# Setup node parsers
simple_node_parser, sentence_node_parser, hierarchical_node_parser, semantic_splitter_node_parser = setup_parser()

# Print the number of documents loaded
print(len(documents))

print(documents)
len(documents)

# Get nodes from documents using different parsers
simple_nodes = simple_node_parser.get_nodes_from_documents(documents)
sentence_nodes = sentence_node_parser.get_nodes_from_documents(documents)
hierarchical_nodes = hierarchical_node_parser.get_nodes_from_documents(documents)
semantic_splitter_nodes = semantic_splitter_node_parser.get_nodes_from_documents(documents)

# Print the number of nodes created by each parser
len(simple_nodes) # 9
len(sentence_nodes) # 222
len(hierarchical_nodes) #82
len(semantic_splitter_nodes) #16

# Set the LLM, embedding model, and prompt helper in settings
Settings.llm = llm
Settings.embed_model = embed_model
Settings.prompt_helper = prompt_helper
def index_creation(simple_node_parser, sentence_node_parser, hierarchical_node_parser, semantic_splitter_node_parser, llm, embed_model, prompt_helper):
    # Create indices from documents using different node parsers
    simple_node_parser_index = VectorStoreIndex.from_documents(
        documents,
        node_parser=simple_node_parser
        )
    sentence_node_parser_index = VectorStoreIndex.from_documents(
        documents,
        node_parser=sentence_node_parser
        )
    hierarchical_node_parser_index = VectorStoreIndex.from_documents(
        documents,
        node_parser=hierarchical_node_parser
        )
    semantic_splitter_node_parser_index = VectorStoreIndex.from_documents(
        documents,
        node_parser=semantic_splitter_node_parser
        )
    return simple_node_parser_index, sentence_node_parser_index, hierarchical_node_parser_index, semantic_splitter_node_parser_index

# Create indices using different node parsers
simple_node_parser_index, sentence_node_parser_index, hierarchical_node_parser_index, semantic_splitter_node_parser_index = index_creation(simple_node_parser, sentence_node_parser, hierarchical_node_parser, semantic_splitter_node_parser, llm, embed_model, prompt_helper)

# Create query engines
def create_query_engine(simple_node_parser_index, sentence_node_parser_index, hierarchical_node_parser_index, semantic_splitter_node_parser_index):
    ########### Creating query engine #########
    simple_engine = simple_node_parser_index.as_query_engine(similarity_top_k=10, streaming=True)
    sentence_engine = sentence_node_parser_index.as_query_engine(similarity_top_k=10,
                                                            node_postprocessors=[
                                                            MetadataReplacementPostProcessor(
                                                             target_metadata_key="window")
                                                             ],streaming=True)
    hierarchical_engine = hierarchical_node_parser_index.as_query_engine(similarity_top_k=10, streaming=True)
    semantic_engine = semantic_splitter_node_parser_index.as_query_engine(similarity_top_k=10, streaming=True)
    return simple_engine, sentence_engine, hierarchical_engine, semantic_engine
simple_engine, sentence_engine, hierarchical_engine, semantic_engine = create_query_engine(simple_node_parser_index, sentence_node_parser_index, hierarchical_node_parser_index, semantic_splitter_node_parser_index)




# List of queries to be executed
All_queries = ['Summary about the document',
               'What are mutual funds bought?',
               'What is the name?',
               'what is Folio number?'
               ]


from datetime import datetime
dt = datetime.now().strftime("%Y_%m_%d %H_%M_%S")
maindf = pd.DataFrame()
dict_out = []

# Open a file to write the query responses
with open(r'D:\RAG_langchain\mf_report_' + dt + '.txt', 'w') as f:
    for query in All_queries:
        # Execute queries using different engines
        simple_response = simple_engine.query(query)
        sentence_response = sentence_engine.query(query)
        hierarchical_response = hierarchical_engine.query(query)
        semantic_response = semantic_engine.query(query)

        # Append responses to the dictionary
        dict_out.append({"query":query,"simple_response":simple_engine.query(query),"sentence_response":sentence_engine.query(query),"hierarchical_response":hierarchical_engine.query(query),"semantic_response":semantic_engine.query(query)})

        # Create a DataFrame from the responses
        df = pd.DataFrame([{"query":query,"simple_response":simple_response,"sentence_response":sentence_response,"hierarchical_response":hierarchical_response,"semantic_response":semantic_response}])
        maindf= pd.concat([maindf,df])

        # Write responses to the file
        f.write(f"{query}\n\n")
        f.write(f"#### simple_response #### \n")
        f.write(f"{simple_response}\n\n")
        f.write(f"#### sentence_response #### \n")
        f.write(f"{sentence_response}\n\n")
        f.write(f"#### hierarchical_response #### \n")
        f.write(f"{hierarchical_response}\n\n")
        f.write(f"#### semantic_response #### \n")
        f.write(f"{semantic_response}\n\n")
        f.write(f"\n\n\n####################################\n\n\n\n\n\n")

# Save the responses to a CSV file
maindf.to_csv(r'D:\RAG_langchain\mf_report_' + dt + '.csv', index=False)




# Extract metadata from the sentence response
window = sentence_response.source_nodes[0].node.metadata["window"]
sentence = sentence_response.source_nodes[0].node.metadata["original_sentence"]

# Print the extracted metadata
print(f"Window: {window}")
print("------------------")
print(f"Original Sentence: {sentence}")


# Print the original sentences from the source nodes
for source_node in sentence_response.source_nodes:
    print(source_node.node.metadata["original_sentence"])
    print("--------")





import nest_asyncio
nest_asyncio.apply()

# Reinitialize the sentence node parser with a different window size
sentence_node_parser = SentenceWindowNodeParser.from_defaults(
    # how many sentences on either side to capture
    window_size=10,
    # the metadata key that holds the window of surrounding sentences
    window_metadata_key="window",
    # the metadata key that holds the original sentence
    original_text_metadata_key="original_sentence",
)

# Create a new index using the sentence node parser
sentence_node_parser_index = VectorStoreIndex.from_documents(
    documents,
    use_async=True,
    node_parser=sentence_node_parser
)

from llama_index.core.postprocessor import TimeWeightedPostprocessor

# Create a new query engine with additional postprocessors
sentence_engine = sentence_node_parser_index.as_query_engine(similarity_top_k=10,
                                                             node_postprocessors=[
                                                                 MetadataReplacementPostProcessor(
                                                                     target_metadata_key="window"),
                                                                 # TimeWeightedPostprocessor(
                                                                 #     time_decay=0.5, time_access_refresh=False, top_k=1
                                                                 # )
                                                             ], streaming=True)

# Execute a query using the new query engine
res = sentence_engine.query(query)
print(res)

from llama_index.core.postprocessor import SimilarityPostprocessor

# Retrieve nodes using the sentence node parser index
nodes = sentence_node_parser_index.as_retriever().retrieve(query)

# Filter nodes below a similarity score of 0.75
processor = SimilarityPostprocessor(similarity_cutoff=0.75)
filtered_nodes = processor.postprocess_nodes(nodes)



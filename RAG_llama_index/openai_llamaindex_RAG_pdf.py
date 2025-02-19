import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core import Settings
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
# from dotenv import load_dotenv

# Load environment variables
# load_dotenv()



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


Settings.llm = OpenAI(temperature=0.1, model="gpt-3.5-turbo", api_key = "**************************************************************************")

Settings.embed_model = OpenAIEmbedding(api_key = "**************************************************************************")

# settings = configure_settings()

# Specify your PDF directory
pdf_directory = r"D:\ALM\Vincent\Archive (1)\New folder"

# Create index
index = load_and_index_documents(pdf_directory)

print(index)

# Create query engine
query_engine = create_query_engine(index)

question = "What is the main topic of the document?"

"""Ask questions and get responses"""
response = query_engine.query(question)
print(response)

print(f"\nQuestion: {question}")
print(f"Answer: {response.response}\n")
print(f"Answer: {response.metadata}\n")
print(f"Answer: {response.source_nodes}\n")

# print(f"\nQuestion: {question}")
# Question: What is the main topic of the document?
# print(f"Answer: {response.response}\n")
# Answer: The main topic of the document is a legal complaint related to a contract dispute, specifically involving a case between 13148 WVICTORY BLVD LLC and ZOHRABIANS ARCHITECTS AND BUILDERS, INC. The complaint outlines various details such as the unknown names of defendants, compliance with claims statutes, the court's jurisdiction, causes of action like breach of contract, and the requested relief including damages and attorney's fees.
# response.metadata
# {'5f52b63a-d208-4c34-99c8-d3674e62261f': {'page_label': '4', 'file_name': '25NNCV00617.pdf', 'file_path': 'D:\\ALM\\Vincent\\Archive (1)\\New folder\\25NNCV00617.pdf', 'file_type': 'application/pdf', 'file_size': 1381787, 'creation_date': '2025-02-19', 'last_modified_date': '2025-02-04'}, 'd594a6f3-c976-4dd7-ac65-058e439f99f4': {'page_label': '2', 'file_name': '25NNCV00617.pdf', 'file_path': 'D:\\ALM\\Vincent\\Archive (1)\\New folder\\25NNCV00617.pdf', 'file_type': 'application/pdf', 'file_size': 1381787, 'creation_date': '2025-02-19', 'last_modified_date': '2025-02-04'}}
# print(f"Answer: {response.metadata}\n")
# Answer: {'5f52b63a-d208-4c34-99c8-d3674e62261f': {'page_label': '4', 'file_name': '25NNCV00617.pdf', 'file_path': 'D:\\ALM\\Vincent\\Archive (1)\\New folder\\25NNCV00617.pdf', 'file_type': 'application/pdf', 'file_size': 1381787, 'creation_date': '2025-02-19', 'last_modified_date': '2025-02-04'}, 'd594a6f3-c976-4dd7-ac65-058e439f99f4': {'page_label': '2', 'file_name': '25NNCV00617.pdf', 'file_path': 'D:\\ALM\\Vincent\\Archive (1)\\New folder\\25NNCV00617.pdf', 'file_type': 'application/pdf', 'file_size': 1381787, 'creation_date': '2025-02-19', 'last_modified_date': '2025-02-04'}}
# response.source_nodes
# [NodeWithScore(node=TextNode(id_='5f52b63a-d208-4c34-99c8-d3674e62261f', embedding=None, metadata={'page_label': '4', 'file_name': '25NNCV00617.pdf', 'file_path': 'D:\\ALM\\Vincent\\Archive (1)\\New folder\\25NNCV00617.pdf', 'file_type': 'application/pdf', 'file_size': 1381787, 'creation_date': '2025-02-19', 'last_modified_date': '2025-02-04'}, excluded_embed_metadata_keys=['file_name', 'file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date'], excluded_llm_metadata_keys=['file_name', 'file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date'], relationships={<NodeRelationship.SOURCE: '1'>: RelatedNodeInfo(node_id='c79826a6-e9ff-464b-9998-214e9c1f3e9b', node_type='4', metadata={'page_label': '4', 'file_name': '25NNCV00617.pdf', 'file_path': 'D:\\ALM\\Vincent\\Archive (1)\\New folder\\25NNCV00617.pdf', 'file_type': 'application/pdf', 'file_size': 1381787, 'creation_date': '2025-02-19', 'last_modified_date': '2025-02-04'}, hash='c299e22e87f17fefbaaf9b0aa8c7380a0d86212472547fcc89dbee49d39bb919')}, metadata_template='{key}: {value}', metadata_separator='\n', text="UNDERLYING AGREEMENT \nWITH SCOPE OF WORK AND \nPAYMENT TERMS \nEXHIBIT ''A''", mimetype='text/plain', start_char_idx=0, end_char_idx=74, metadata_seperator='\n', text_template='{metadata_str}\n\n{content}'), score=0.7706270391647948), NodeWithScore(node=TextNode(id_='d594a6f3-c976-4dd7-ac65-058e439f99f4', embedding=None, metadata={'page_label': '2', 'file_name': '25NNCV00617.pdf', 'file_path': 'D:\\ALM\\Vincent\\Archive (1)\\New folder\\25NNCV00617.pdf', 'file_type': 'application/pdf', 'file_size': 1381787, 'creation_date': '2025-02-19', 'last_modified_date': '2025-02-04'}, excluded_embed_metadata_keys=['file_name', 'file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date'], excluded_llm_metadata_keys=['file_name', 'file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date'], relationships={<NodeRelationship.SOURCE: '1'>: RelatedNodeInfo(node_id='a8feca5f-85a7-4501-80b6-3cfb8c46c102', node_type='4', metadata={'page_label': '2', 'file_name': '25NNCV00617.pdf', 'file_path': 'D:\\ALM\\Vincent\\Archive (1)\\New folder\\25NNCV00617.pdf', 'file_type': 'application/pdf', 'file_size': 1381787, 'creation_date': '2025-02-19', 'last_modified_date': '2025-02-04'}, hash='38a7cc3c47da69eaedea444cdfd3dc359db3a85619b8ed699803b10e81c9e072')}, metadata_template='{key}: {value}', metadata_separator='\n', text="PLD -C-001 \nSHORT TITLE: C A SE NUMBER: \n13148 WVICTORY BLVD LLC v. ZOHRABIANS ARCHITECTS AND BUILDERS, INC . \n4. b. The true names of defendants sued as Does are unknown to plaintiff. \n(1) [RJ Doe defendants (specify Doe numbers): 1 -49 were the agents or employees of the named \ndefendants and acted within the scope of that agency or employment. \n(2) [RJ Doe defendants (specify Doe numbers): 50 - 100 are persons whose capacities are unknown to \nplaintiff. \nc. c=J Information about additional defendants who are not natural persons is contained in Attachment 4c. \nd. c=J Defendants who are joined under Code of Civil Procedure section 382 are (names): \n5. c=J Plaintiff is required to comply with a claims statute, and \na. c=J has complied with applicable claims statutes, or \nb. c=J is excused from complying because (specify): \n6. c=J This action is subject to c=J Civil Code section 1812.10 c=J Civil Code section 2984.4. \n7. This court is the proper court because \na. [KJ a defendant entered into the contract here. \nb. c=J a defendant lived here when the contract was entered into. \nc. c=J a defendant lives here now. \nd. [KJ the contract was to be performed here. \ne. [KJ a defendant is a corporation or unincorporated association and its principal place of business is here. \nf. c=J real property that is the subject of this action is located here. \ng. c=J other (specify): \n8. The following causes of action are attached and the statements above apply to each (each complaint must have one or \nmore causes of action attached): \n[KJ Breach of Contract \nc=J Common Counts \nc=J Other (specify): \n9. c=J Other allegations: \n10. Plaintiff prays for judgment for costs of suit; for such relief as is fair, just, and equitable; and for \na. [8] damages of: $180,000.00 \nb. III interest on the damages \n(1) [RJ according to proof \n(2) c=J at the rate of (specify): percent per year from (date): \nc. c=J attorney's fees \n(1) c=J of: $ \n(2) c=J according to proof. \nd. III other (specify): \nLoss of Investment and Opportunity Costs Due to Defendant's Failure to Complete Required Scope of Work \n11. [KJ The paragraphs of this pleading alleged on information and belief are as follows (specify paragraph numbers): \nDate Janu::y\n1\n:9. 2025 II.. [\\ ·, .,-\nOmar J. Yassin, Esq. ,. ~ \n(TYPE OR PRINT N A ME) (SIGNATURE \n(If you wish to verify this pleading, affix a verification.) \nPLD -C-001 [Rev. January 1, 2024] COMPLA INT - Contract Page 2 of 2", mimetype='text/plain', start_char_idx=0, end_char_idx=2446, metadata_seperator='\n', text_template='{metadata_str}\n\n{content}'), score=0.7468707851544845)]


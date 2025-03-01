from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings


# Function to extract data from PDF files in a specified directory.
# It loads all PDF documents present in the given directory using PyPDFLoader.
# Parameters:
# - data (str): Path to the directory containing PDF files.
# Returns:
# - List of loaded documents.
def load_pdf_file(data):
    loader = DirectoryLoader(data,
                             glob="*.pdf",
                             loader_cls=PyPDFLoader)
    
    documents = loader.load()
    return documents


# Function to split extracted text into smaller chunks for processing.
# It uses RecursiveCharacterTextSplitter to divide the text into chunks of specified size.
# Parameters:
# - extracted_data (list): List of extracted documents.
# Returns:
# - List of text chunks.
def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500,
                                                   chunk_overlap=20)
    text_chunks = text_splitter.split_documents(extracted_data)
    
    return text_chunks


# Function to download pre-trained Hugging Face embeddings.
# It loads the 'sentence-transformers/all-MiniLM-L6-V2' model, which provides 
# 384-dimensional embeddings for text processing.
# Parameters:
# - None
# Returns:
# - HuggingFaceEmbeddings object containing the embedding model.
def download_hugging_face_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-V2')  # 384-dimensional vector
    return embeddings

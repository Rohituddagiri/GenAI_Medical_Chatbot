from src.helper import load_pdf_file, text_split, download_hugging_face_embeddings
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Retrieve Pinecone API key from environment variables
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY  # Ensure API key is set in the environment

# Step 1: Extract text data from PDF files in the "data/" directory
extracted_data = load_pdf_file(data="data/")

# Step 2: Split extracted text into smaller chunks for better processing
text_chunks = text_split(extracted_data)

# Step 3: Load pre-trained Hugging Face embeddings model for vector representation
embeddings = download_hugging_face_embeddings()

# Step 4: Initialize Pinecone client with API key
pc = Pinecone(api_key=os.environ.get('PINECONE_API_KEY'))

# Define the name of the Pinecone index where embeddings will be stored
index_name = "medibot"

# Step 5: Create a new Pinecone index for storing vector embeddings
pc.create_index(
    name=index_name,
    dimension=384,  # Embedding dimension of the model used
    metric="cosine",  # Use cosine similarity for nearest neighbor search
    spec=ServerlessSpec(
        cloud="aws",  # Deploying on AWS
        region="us-east-1"  # AWS region for the Pinecone index
    ) 
)

# Step 6: Store the text chunks into Pinecone as vector embeddings
docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings
)
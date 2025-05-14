# agents/retriever_agent.py

from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader

def build_vector_index():
    loader = TextLoader("data/earnings_sample.txt")
    documents = loader.load()
    
    text_splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    docs = text_splitter.split_documents(documents)

    db = FAISS.from_documents(docs, OpenAIEmbeddings())
    return db

def retrieve_relevant_chunks(query):
    db = build_vector_index()
    return db.similarity_search(query, k=2)

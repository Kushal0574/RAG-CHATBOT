from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from rag.loader import load_documents

_vectorstore = None

def get_vectorstore():
    global _vectorstore
    if _vectorstore is None:
        docs = load_documents()
        embeddings = OpenAIEmbeddings()
        _vectorstore = FAISS.from_documents(docs, embeddings)
    return _vectorstore

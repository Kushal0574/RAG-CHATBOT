from rag.vectorstore import get_vectorstore
from rag.llm import get_llm

def run_rag(query: str) -> str:
    vectordb = get_vectorstore()
    docs = vectordb.similarity_search(query, k=3)

    context = "\n\n".join(d.page_content for d in docs)

    llm = get_llm()
    prompt = f"""Use the context below to answer the question.

Context:
{context}

Question:
{query}
"""
    return llm.invoke(prompt)

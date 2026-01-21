import streamlit as st
from rag.pipeline import run_rag

st.set_page_config(page_title="RAG Chatbot")
st.title("📄 RAG Chatbot on Documentation")

query = st.text_input("Ask a question about the documents:")

if query:
    answer = run_rag(query)
    st.markdown("### Answer")
    st.write(answer)

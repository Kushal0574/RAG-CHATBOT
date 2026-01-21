# RAG Chatbot on Real Documentation

## Overview
This project implements a Retrieval-Augmented Generation (RAG) chatbot over real documentation using LangChain.

## Stack
- Python
- LangChain
- FAISS vector database
- OpenAI LLM
- Streamlit frontend

## How It Works
1. Load and chunk documentation
2. Embed chunks into vector database
3. Retrieve relevant chunks for a query
4. Generate answer using LLM + retrieved context

## Setup
```bash
pip install -r requirements.txt
export OPENAI_API_KEY=your_key_here
streamlit run app.py
```

## Resume Value
Demonstrates RAG pipelines, vector search, LLM orchestration, and full-stack AI apps.

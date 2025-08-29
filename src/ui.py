import streamlit as st
from rag_pipeline import RAGPipeline

st.title("📘 Personal Knowledge Assistant")

pipeline = RAGPipeline("sentence-transformers/all-MiniLM-L6-v2", "google/flan-t5-base")

uploaded = st.file_uploader("Upload a document", type=["pdf", "txt"])
if uploaded:
    text = uploaded.read().decode("utf-8")
    pipeline.build_index([text])
    st.success("Document ingested!")

query = st.text_input("Ask a question:")
if query:
    answer = pipeline.query(query)
    st.write("**Answer:**", answer)

# 📘 Personal Knowledge Assistant (RAG)

An intelligent **Retrieval-Augmented Generation (RAG)** system that ingests PDFs, notes, and web content to provide **context-aware, source-backed answers**.  
Built with modular components for **scalable ingestion, semantic retrieval, and multi-turn dialogue**.  

---

## ✨ Features
- 🔹 **RAG Pipeline** → Semantic retrieval with SentenceTransformers + FAISS, generation with FLAN-T5.  
- 🔹 **Multi-source ingestion** → PDFs, text, markdown, HTML, and URLs.  
- 🔹 **Preprocessing** → Cleaning, chunking with overlaps, and metadata tagging.  
- 🔹 **Context-aware answers** → Queries resolved with relevant context and **explicit source citations**.  
- 🔹 **Multi-turn chat** → Maintains dialogue history across turns for interactive use.  
- 🔹 **Deployment options** → CLI, FastAPI API, and Streamlit web UI.  
- 🔹 **Persistence** → Save/load vector indexes (`outputs/index`).  

---

## 🛠️ Installation
```bash
# Clone repo and enter folder
git clone https://github.com/<your-username>/personal-knowledge-assistant.git
cd personal-knowledge-assistant

# Create virtual environment
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

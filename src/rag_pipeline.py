from ingestion import load_pdf, load_txt
from preprocessing import clean_text, chunk_text
from embeddings import Embedder
from vectordb import VectorDB
from retriever import retrieve
from generator import Generator

class RAGPipeline:
    def __init__(self, embed_model, llm_model):
        self.embedder = Embedder(embed_model)
        self.generator = Generator(llm_model)
        self.vectordb = None

    def build_index(self, texts):
        clean_chunks = []
        for text in texts:
            clean_chunks.extend(chunk_text(clean_text(text)))
        embeddings = self.embedder.encode(clean_chunks)
        self.vectordb = VectorDB(embeddings.shape[1])
        self.vectordb.add(embeddings, clean_chunks)

    def query(self, question, top_k=5):
        results = retrieve(question, self.embedder, self.vectordb, top_k)
        context = " ".join([r[0] for r in results])
        return self.generator.generate(question, context)

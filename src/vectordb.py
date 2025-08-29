import faiss
import numpy as np

class VectorDB:
    def __init__(self, dim):
        self.index = faiss.IndexFlat2(dim)
        self.docs = []

    def add(self, embeddings, texts):
        self.index.add(np.array(embeddings))
        self.docs.extend(texts)
    
    def search(self, query_embedding, top_k=5):
        D, I = self.index.search(np.array([query_embedding]), top_k)
        return [(self.docs[i], float(D[0][j])) for j, i in enumerate(I[0])]
    
    
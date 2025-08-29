from sentence_transformers import SentenceTransformer

class Embedder:
    def __init__(self, model_name = "sentence_transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
    
    def encode(self, texts):
        return self.model.encode(texts, convert_to_numpy=True)

    def embed(self, texts):
        return self.encode(texts)

    def embed_query(self, query):
        return self.embed([query])
    
    
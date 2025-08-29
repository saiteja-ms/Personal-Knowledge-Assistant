def retrieve(query, embedder, vectordb, top_k=5):
    q_emb = embedder.encode([query])[0]
    results = vectordb.search(q_emb, top_k=top_k)
    return results

from transformers import pipeline

class Generator:
    def __init__(self, model_name="google/flan-t5-base"):
        self.pipe = pipeline("text2text-generation", model=model_name)
    
    def generate(self, query, context):
        prompt = f"Answer the question using the context. \nContext: {context}\n\nQuestion: {query}"
        response = self.pipe(prompt, max_length=256, truncation=True)
        return response[0]['generated_text']
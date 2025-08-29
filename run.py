import os
from src.rag_pipeline import RAGPipeline 

def main():
    cfg = os.path.join(os.path.dirname(__file__), 'config.yaml')
    rag = RAGPipeline(cfg)
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    docs = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith(('.txt', '.md', '.markdown', '.pdf', '.html','.htm'))]
    if not docs:
        sample = os.path.join(data_dir, 'sample.txt')
        with open(sample, 'w') as f:
            f.write('This is a sample knowledge base. Add your PDFs and notes to the data/folder.')
        docs = [sample]
    rag.build_index_from_paths(docs, index_dir= os.path.join(os.path.dirname(__file__), 'outputs', 'index'))
    print('Index built. Ask questions (type exit to quite).')
    while True:
        q = input('You: ')
        if q.lower().strip() in {'exit', 'quit'}:
            break 
        print('Bot:', rag.answer(q))

if __name__ == '__main__':
    main()
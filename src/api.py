from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
import os, tempfile, shutil
from typing import List, Optional 
from .rag_pipeline import RAGPipeline

app = FastAPI(title="Personal Knowledge Assistant API")
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config.yaml")
pipeline = RAGPipeline(CONFIG_PATH)

@app.post("/ingest/files")
async def ingest_files(files: List[UploadFile]):
    tmpdir = tempfile.mkdtemp()
    paths = []
    try:
        for f in files:
            dest = os.path.join(tmpdir, f.filename)
            with open(dest, "wb") as out:
                out.write(await f.read())
            paths.append(dest)
        pipeline.build_index_from_paths(paths, index_dir=os.path.join(tmpdir, "index"))
        # persist index to project outputs for reuse
        out_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "outputs", "index"))
        os.makedirs(out_dir, exist_ok=True)
        shutil.copy(os.path.join(tmpdir, "index", "faiss.index"), os.path.join(out_dir, "faiss.index"))
        shutil.copy(os.path.join(tmpdir, "index", "meta.json"), os.path.join(out_dir, "meta.json"))
        return {"message": "Indexed documents", "count": len(paths)}
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)

@app.post("/ingest/urls")
async def ingest_urls(urls: List[str]):
    pipeline.build_index_from_paths(urls, index_dir=os.path.join(os.path.dirname(__file__), "..", "outputs", "index"))
    return {"message": "Indexed URLs", "count": len(urls)}

@app.post("/load_index")
async def load_index():
    idx_dir = os.path.join(os.path.dirname(__file__), "..", "outputs", "index")
    pipeline.load_index(idx_dir)
    return {"message": "Index loaded"}

@app.get("/query")
async def query(q: str, session_id: Optional[str] = "default", top_k: Optional[int] = None):
    try:
        ans = pipeline.answer(q, session_id = session_id, top_k = top_k)
        return {"answer": ans}
    except AssertionError as e:
        return JSONResponse(status_code=400, content={"error": str(e)})
    


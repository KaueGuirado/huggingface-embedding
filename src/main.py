from fastapi import FastAPI
from src.models import Embedding
from langchain_community.embeddings import HuggingFaceEmbeddings

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

model_name = "BAAI/bge-m3"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}
hf = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

@app.post("/embedding")
def embedding(embedding: Embedding):
    embedded = hf.embed_query(embedding.text)
    return {"embedded": embedded}
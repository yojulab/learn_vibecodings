from fastapi import FastAPI
from .routes import posts

app = FastAPI()

app.include_router(posts.router, prefix="/posts", tags=["posts"])

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

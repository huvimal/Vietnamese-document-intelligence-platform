from fastapi import FastAPI
from app.routes import upload

app = FastAPI(title="Vietnamese Document Intelligence Platform")

app.include_router(upload.router)

@app.get("/")
def root():
    return {
        "message": "Vietnamese Document Intelligence Platform API"
    }
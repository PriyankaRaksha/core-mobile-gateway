# Arjun(Backend)
from fastapi import FastAPI
from app.routes import auth

app = FastAPI()

app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"message": "Core Mobile Gateway API running"}

@app.get("/health")
def health():
    return {"status": "ok"}
#Arjun(Backend)
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Core Mobile Gateway API running"}

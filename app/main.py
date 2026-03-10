#Arjun(Backend)
from fastapi import FastAPI
from app.users import get_users

app = FastAPI()

@app.get("/")
def home():
    return {"service": "core mobile gateway"}

@app.get("/users")
def users():
    return get_users()
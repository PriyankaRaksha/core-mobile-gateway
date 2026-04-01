from fastapi import APIRouter

router = APIRouter()

users = []

@router.post("/users")
def create_user(name:str):
    users.append(name)
    return {"user":name}
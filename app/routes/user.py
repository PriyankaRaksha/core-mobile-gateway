from fastapi import APIRouter
from app.services.user_service import add_user

router = APIRouter()

users = []

@router.post("/users")
def create_user(name:str):
    return add_user(name)



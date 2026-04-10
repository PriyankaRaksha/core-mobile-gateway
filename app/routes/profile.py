from fastapi import APIRouter

router = APIRouter()

@router.get("/profile/{username}")
def get_profile(username: str):
    return {
        "username": username,
        "role": "developer",
        "status": "active"
    }
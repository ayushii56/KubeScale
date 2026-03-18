from fastapi import APIRouter
from app.core.security import create_access_token

router = APIRouter(prefix="/api/v1/auth")

@router.get("/health")
def health():
    return {"status": "auth service ok"}

@router.post("/login")
def login():
    token = create_access_token({"sub": "user123"})
    return {"access_token": token}
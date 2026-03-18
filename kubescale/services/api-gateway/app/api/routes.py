from fastapi import APIRouter
import httpx

router = APIRouter(prefix="/api/v1")

@router.get("/")
def root():
    return {"message": "KubeScale API Gateway v1"}

@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.get("/auth/health")
async def auth_health():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://auth-service:8001/api/v1/auth/health")
        return response.json()
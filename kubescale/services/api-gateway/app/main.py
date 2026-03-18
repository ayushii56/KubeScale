from fastapi import FastAPI
from app.api.routes import router
from app.core.config import settings

app = FastAPI(title=settings.app_name)

@app.get("/")
def base():
    return {
        "message": settings.app_name,
        "version": settings.api_version
    }

app.include_router(router)
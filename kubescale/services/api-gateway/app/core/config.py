from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "KubeScale API Gateway"
    api_version: str = "v1"

    class Config:
        env_file = ".env"

settings = Settings()
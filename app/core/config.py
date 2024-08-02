# app/core/config.py

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str
    SMTP_SERVER: str = "localhost"
    SMTP_PORT: int = 25
    SMTP_USER: str = None
    SMTP_PASSWORD: str = None

    class Config:
        case_sensitive = True

settings = Settings()

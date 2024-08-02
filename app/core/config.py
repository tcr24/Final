# app/core/config.py

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str = "sqlite:///./test.db"
    SMTP_SERVER: str = "localhost"
    SMTP_PORT: int = 25
    SMTP_USER: str = "user@example.com"
    SMTP_PASSWORD: str = "password"

    class Config:
        case_sensitive = True

settings = Settings()

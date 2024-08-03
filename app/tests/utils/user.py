from typing import Dict
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.schemas.user_schemas import UserCreate
from app.models.user import User
from app.services.user_service import UserService

def create_random_user(db: Session, is_superuser: bool = False) -> User:
    user_in = UserCreate(
        email="user@example.com",
        password="password123",
        full_name="Test User",
        nickname="testuser",
        is_active=True,
        is_superuser=is_superuser,
    )
    user = UserService.create(db, user_in)
    return user

def authentication_token_from_email(client: TestClient, email: str) -> str:
    login_data = {
        "username": email,
        "password": "password123",
    }
    response = client.post("/login/access-token", data=login_data)
    tokens = response.json()
    return tokens["access_token"]

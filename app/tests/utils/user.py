# app/tests/utils/user.py

from sqlalchemy.orm import Session
from fastapi.testclient import TestClient
from app import crud, schemas
from app.models import User
from app.tests.utils.utils import random_email, random_lower_string
from app.core.config import settings

def create_random_user(db: Session, *, is_superuser: bool = False) -> User:
    email = random_email()
    password = random_lower_string()
    user_in = schemas.UserCreate(
        email=email,
        password=password,
        is_superuser=is_superuser,
    )
    user = crud.user.create(db, obj_in=user_in)
    return user

def authentication_token_from_email(client: TestClient, email: str) -> str:
    login_data = {
        "username": email,
        "password": settings.TEST_USER_PASSWORD,
    }
    r = client.post(f"{settings.API_V1_STR}/login/access-token", data=login_data)
    tokens = r.json()
    return tokens["access_token"]

from app.models.user_model import User, UserRole
from app.schemas.user import UserCreate
from app.utils.security import hash_password
from sqlalchemy.orm import Session
import random
import string

def create_random_user(db_session: Session, is_admin: bool = False) -> User:
    email = "".join(random.choices(string.ascii_lowercase + string.digits, k=10)) + "@example.com"
    user_in = UserCreate(
        email=email,
        password="password123",
        first_name="First",
        last_name="Last",
        nickname="nickname"
    )
    user = User(
        email=user_in.email,
        hashed_password=hash_password(user_in.password),
        first_name=user_in.first_name,
        last_name=user_in.last_name,
        nickname=user_in.nickname,
        role=UserRole.ADMIN if is_admin else UserRole.USER,
        email_verified=True
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user

from fastapi.testclient import TestClient

def authentication_token_from_email(client: TestClient, email: str) -> str:
    data = {"username": email, "password": "password123"}
    response = client.post(f"{settings.API_V1_STR}/login/access-token", data=data)
    assert response.status_code == 200
    return response.json()["access_token"]

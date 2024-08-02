import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core.config import settings
from app.tests.utils.user import create_random_user, authentication_token_from_email
from sqlalchemy.orm import Session
from app import crud, schemas

client = TestClient(app)

def test_update_profile(db: Session) -> None:
    user = create_random_user(db)
    access_token = authentication_token_from_email(client, user.email)
    headers = {"Authorization": f"Bearer {access_token}"}
    new_bio = "This is my new bio"
    response = client.put(
        f"{settings.API_V1_STR}/users/profile",
        headers=headers,
        json={"bio": new_bio},
    )
    assert response.status_code == 200
    content = response.json()
    assert content["bio"] == new_bio

def test_upgrade_user_to_pro(db: Session) -> None:
    superuser = create_random_user(db, is_superuser=True)
    user = create_random_user(db)
    access_token = authentication_token_from_email(client, superuser.email)
    headers = {"Authorization": f"Bearer {access_token}"}
    response = client.put(
        f"{settings.API_V1_STR}/users/upgrade/{user.id}",
        headers=headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["is_pro"] is True

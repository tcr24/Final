import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user_model import User
from app.utils.security import hash_password

@pytest.fixture(scope="function")
async def test_bulk_user_creation_performance(db_session: AsyncSession):
    users = []
    for i in range(100):
        user = User(
            email=f"user{i}@example.com",
            hashed_password=hash_password("password123"),
            first_name=f"First{i}",
            last_name=f"Last{i}",
            nickname=f"nickname{i}",
            email_verified=True
        )
        users.append(user)
        db_session.add(user)
    await db_session.commit()
    assert len(users) == 100

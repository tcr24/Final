from app.database import get_db

async def get_db_session():
    async for session in get_db():
        yield session

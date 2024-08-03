from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from pydantic import BaseSettings

Base = declarative_base()

class Settings(BaseSettings):
    database_url: str

settings = Settings(_env_file='.env')

engine = create_async_engine(settings.database_url, echo=True)
AsyncSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession
)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

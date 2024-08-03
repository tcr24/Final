from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models.user_model import User
from sqlalchemy.future import select
from typing import List

router = APIRouter()

@router.get("/users/", response_model=List[User])
async def read_users(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).offset(skip).limit(limit))
    users = result.scalars().all()
    return users

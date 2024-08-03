# app/schemas/user.py

from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    nickname: str

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int

    class Config:
        orm_mode = True  # For SQLAlchemy models compatibility

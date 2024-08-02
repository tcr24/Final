from sqlalchemy import Boolean, Column, Integer, String
from app.db.base_class import Base

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    is_pro = Column(Boolean, default=False)
    bio = Column(String, nullable=True)
    location = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
    is_superuser = Column(Boolean, default=False)

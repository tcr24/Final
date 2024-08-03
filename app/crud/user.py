from sqlalchemy.orm import Session
from app.models.user_model import User
from uuid import UUID

def get_user_by_id(db: Session, user_id: UUID) -> User:
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str) -> User:
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: User) -> User:
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def update_user(db: Session, user: User) -> User:
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user: User) -> None:
    db.delete(user)
    db.commit()

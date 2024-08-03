from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.api import deps
from app.core.config import settings

router = APIRouter()

@router.put("/profile", response_model=schemas.User)
def update_profile(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.UserUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update own profile.
    """
    user = crud.user.update(db=db, db_obj=current_user, obj_in=user_in)
    return user

@router.put("/upgrade/{user_id}", response_model=schemas.User)
def upgrade_user_to_pro(
    *,
    db: Session = Depends(deps.get_db),
    user_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Upgrade user to professional status.
    """
    if not crud.user.is_superuser(current_user):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The user doesn't have enough privileges",
        )
    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    user = crud.user.update(db=db, db_obj=user, obj_in={"is_pro": True})
    return user

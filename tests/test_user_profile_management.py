import pytest
from sqlalchemy.orm import Session
from app.tests.utils.user import create_random_user, authentication_token_from_email
from app.models.user_model import UserRole

def test_update_profile(db_session: Session) -> None:
    user = create_random_user(db_session)
    # Perform profile update actions here...
    # For example:
    user.first_name = "UpdatedFirstName"
    db_session.commit()
    db_session.refresh(user)
    assert user.first_name == "UpdatedFirstName"

def test_upgrade_user_to_pro(db_session: Session) -> None:
    superuser = create_random_user(db_session, is_admin=True)
    # Perform user upgrade actions here...
    # For example:
    superuser.role = UserRole.PRO
    db_session.commit()
    db_session.refresh(superuser)
    assert superuser.role == UserRole.PRO

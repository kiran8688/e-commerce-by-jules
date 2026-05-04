from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import create_access_token, hash_password, verify_password
from app.models.user import User
from app.schemas.auth import UserCreate


async def create_user(db: AsyncSession, payload: UserCreate) -> User:
    """
    Create a new user with a hashed password.
    Business rules should live here, not in the router.
    """
    user = User(
        email=payload.email,
        hashed_password=hash_password(payload.password),
        full_name=payload.full_name,
        phone=payload.phone,
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


async def get_user_by_email(db: AsyncSession, email: str) -> User | None:
    """Securely fetch user by email without verifying password."""
    stmt = select(User).where(User.email == email)
    return await db.scalar(stmt)


async def authenticate_user(db: AsyncSession, email: str, password: str) -> User | None:
    """Verify login credentials."""
    stmt = select(User).where(User.email == email)
    user = await db.scalar(stmt)

    if not user:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    return user


def issue_token_for_user(user: User) -> str:
    """Return JWT access token for a user."""
    return create_access_token(subject=str(user.id), extra={"email": user.email, "admin": user.is_admin})

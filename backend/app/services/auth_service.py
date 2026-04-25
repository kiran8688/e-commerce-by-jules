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
    """Retrieve a user by email securely without checking the password."""
    stmt = select(User).where(User.email == email)
    return await db.scalar(stmt)


async def authenticate_user(db: AsyncSession, email: str, password: str) -> User | None:
    """Verify login credentials."""
    user = await get_user_by_email(db, email)

    if not user:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    return user


def issue_token_for_user(user: User) -> str:
    """Return JWT access token for a user."""
    return create_access_token(subject=str(user.id), extra={"email": user.email, "admin": user.is_admin})

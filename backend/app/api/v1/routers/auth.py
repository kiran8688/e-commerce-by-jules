from app.db.session import get_db
from app.schemas.auth import TokenResponse, UserCreate, UserLogin, UserOut
from app.services.auth_service import (
    authenticate_user,
    create_user,
    get_user_by_email,
    issue_token_for_user,
)
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def register(payload: UserCreate, db: AsyncSession = Depends(get_db)):
    """
    Register a new customer account.

    Workflow:
    1. Check if the user already exists to prevent duplicate account creation.
    2. If not, delegate to `auth_service.create_user` to handle password hashing and DB insertion.

    Status Codes:
    - 201 Created: Successfully registered.
    - 409 Conflict: Email already in use.
    - 422 Unprocessable Entity: Pydantic validation failed (e.g., weak password, invalid email format).
    """
    # Fix: Use get_user_by_email instead of authenticate_user to prevent a timing attack
    # (password oracle vulnerability) and to correctly detect duplicates even if wrong password given.
    existing = await get_user_by_email(db, payload.email)
    if existing:
        raise HTTPException(status_code=409, detail="User already exists")

    return await create_user(db, payload)


@router.post("/login", response_model=TokenResponse)
async def login(payload: UserLogin, db: AsyncSession = Depends(get_db)):
    """
    Validate credentials and mint an access token.
    """
    user = await authenticate_user(db, payload.email, payload.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return TokenResponse(access_token=issue_token_for_user(user))

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.auth import TokenResponse, UserCreate, UserLogin, UserOut
from app.services.auth_service import authenticate_user, create_user, issue_token_for_user

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register(payload: UserCreate, db: Session = Depends(get_db)):
    """
    Register a new customer account.
    """
    existing = authenticate_user(db, payload.email, payload.password)
    if existing:
        raise HTTPException(status_code=409, detail="User already exists")

    return create_user(db, payload)


@router.post("/login", response_model=TokenResponse)
def login(payload: UserLogin, db: Session = Depends(get_db)):
    """
    Validate credentials and mint an access token.
    """
    user = authenticate_user(db, payload.email, payload.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return TokenResponse(access_token=issue_token_for_user(user))

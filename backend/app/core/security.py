from datetime import datetime, timedelta, timezone
from typing import Any

import jwt
from pwdlib import PasswordHash

from app.core.config import settings

# Argon2 is the recommended modern password hashing approach in pwdlib guidance.
password_hasher = PasswordHash.recommended()


def hash_password(password: str) -> str:
    """Hash a plaintext password before storage."""
    return password_hasher.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    """Verify a plaintext password against a stored hash."""
    return password_hasher.verify(password, hashed_password)


def create_access_token(subject: str, expires_minutes: int | None = None, extra: dict[str, Any] | None = None) -> str:
    """
    Create a signed JWT access token.

    Claims:
    - sub: subject identifier
    - exp: expiry timestamp
    """
    expire_delta = timedelta(minutes=expires_minutes or settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    expire = datetime.now(timezone.utc) + expire_delta

    payload: dict[str, Any] = {"sub": subject, "exp": expire}
    if extra:
        payload.update(extra)

    return jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)


def decode_token(token: str) -> dict[str, Any]:
    """Decode and validate a JWT token."""
    return jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])

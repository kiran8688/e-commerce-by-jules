from typing import Annotated

import jwt
from app.core.config import settings
from app.core.security import decode_token
from app.db.session import get_db
from app.models.user import User
from app.schemas.auth import TokenPayload
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_PREFIX}/auth/login")


async def get_current_user(
    db: Annotated[AsyncSession, Depends(get_db)],
    token: Annotated[str, Depends(reusable_oauth2)],
) -> User:
    try:
        payload = decode_token(token)
        token_data = TokenPayload(**payload)
    except (jwt.PyJWTError, ValidationError) as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        ) from e

    from sqlalchemy.orm import noload

    # ⚡ Bolt: Prevent massive N+1 query issue.
    # db.get(User) implicitly eagerly loads addresses, orders, reviews, and cart
    # because of lazy="selectin" on the model. noload('*') stops this.
    user = await db.get(User, token_data.sub, options=[noload("*")])

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


async def get_current_active_admin(
    current_user: Annotated[User, Depends(get_current_user)],
) -> User:
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="The user doesn't have enough privileges"
        )
    if not current_user.is_active:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Inactive user")
    return current_user

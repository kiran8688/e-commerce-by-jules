from uuid import UUID

from app.api.v1.deps import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.schemas.cart import CartItemCreate, CartOut
from app.services.cart_service import add_to_cart, get_or_create_cart
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/carts", tags=["Cart"])

def _verify_user_access(current_user: User, target_user_id: UUID) -> None:
    if current_user.id != target_user_id and not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this cart"
        )

@router.get("/{user_id}", response_model=CartOut)
async def read_cart(
    user_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    _verify_user_access(current_user, user_id)
    return await get_or_create_cart(db, user_id)

@router.post("/{user_id}/items", response_model=CartOut)
async def add_item_to_cart(
    user_id: UUID,
    item: CartItemCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    _verify_user_access(current_user, user_id)
    try:
        return await add_to_cart(db, user_id, item)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e)) from e

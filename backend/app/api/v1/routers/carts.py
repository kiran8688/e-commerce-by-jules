from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from app.api.v1.deps import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.schemas.cart import CartOut, CartItemCreate
from app.services.cart_service import get_or_create_cart, add_to_cart

router = APIRouter(prefix="/carts", tags=["Cart"])

@router.get("/{user_id}", response_model=CartOut)
async def read_cart(user_id: UUID, current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    if user_id != current_user.id and not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Not authorized to access this cart")
    return await get_or_create_cart(db, user_id)

@router.post("/{user_id}/items", response_model=CartOut)
async def add_item_to_cart(user_id: UUID, item: CartItemCreate, current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    if user_id != current_user.id and not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Not authorized to modify this cart")
    try:
        return await add_to_cart(db, user_id, item)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from app.db.session import get_db
from app.schemas.cart import CartOut, CartItemCreate
from app.services.cart_service import get_or_create_cart, add_to_cart

router = APIRouter(prefix="/carts", tags=["Cart"])

@router.get("/{user_id}", response_model=CartOut)
async def read_cart(user_id: UUID, db: AsyncSession = Depends(get_db)):
    return await get_or_create_cart(db, user_id)

@router.post("/{user_id}/items", response_model=CartOut)
async def add_item_to_cart(user_id: UUID, item: CartItemCreate, db: AsyncSession = Depends(get_db)):
    try:
        return await add_to_cart(db, user_id, item)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

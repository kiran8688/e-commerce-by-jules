from uuid import UUID

from app.db.session import get_db
from app.models.cart import Cart
from app.schemas.cart import CartItemCreate, CartOut
from app.services.cart_service import add_to_cart, get_or_create_cart
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import raiseload

router = APIRouter(prefix="/carts", tags=["Cart"])

@router.get("/{user_id}", response_model=CartOut)
async def read_cart(user_id: UUID, db: AsyncSession = Depends(get_db)):
    """
    ⚡ Bolt Performance Optimization:
    Apply `raiseload('user')` because CartOut schema only requires `items` and not
    the eagerly loaded `User` relation.
    """
    return await get_or_create_cart(db, user_id, load_options=[raiseload(Cart.user)])

@router.post("/{user_id}/items", response_model=CartOut)
async def add_item_to_cart(user_id: UUID, item: CartItemCreate, db: AsyncSession = Depends(get_db)):
    try:
        return await add_to_cart(db, user_id, item)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

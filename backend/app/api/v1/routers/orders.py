from uuid import UUID

from app.db.session import get_db
from app.models.order import Order
from app.schemas.order import OrderCreate, OrderOut
from app.services.order_service import create_order_from_cart
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/{user_id}", response_model=OrderOut)
async def create_order(user_id: UUID, order_in: OrderCreate, db: AsyncSession = Depends(get_db)):
    try:
        return await create_order_from_cart(db, user_id, order_in)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{user_id}", response_model=list[OrderOut])
async def list_orders(user_id: UUID, db: AsyncSession = Depends(get_db)):
    result = await db.scalars(select(Order).where(Order.user_id == user_id))
    return list(result)

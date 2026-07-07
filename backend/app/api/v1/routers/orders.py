from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID

from app.api.v1.deps import get_current_user
from app.db.session import get_db
from app.models.order import Order
from app.models.user import User
from app.schemas.order import OrderCreate, OrderOut
from app.services.order_service import create_order_from_cart

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/{user_id}", response_model=OrderOut)
async def create_order(user_id: UUID, order_in: OrderCreate, current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    if current_user.id != user_id and not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Not authorized to create an order for this user")
    try:
        return await create_order_from_cart(db, user_id, order_in)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{user_id}", response_model=list[OrderOut])
async def list_orders(user_id: UUID, current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    if current_user.id != user_id and not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Not authorized to access these orders")
    result = await db.scalars(select(Order).where(Order.user_id == user_id))
    return list(result)

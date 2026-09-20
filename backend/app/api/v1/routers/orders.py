from uuid import UUID

from app.api.v1.deps import get_current_user
from app.db.session import get_db
from app.models.order import Order
from app.models.user import User
from app.schemas.order import OrderCreate, OrderOut
from app.services.order_service import create_order_from_cart
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import noload

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/{user_id}", response_model=OrderOut)
async def create_order(
    user_id: UUID,
    order_in: OrderCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if current_user.id != user_id and not current_user.is_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")
    try:
        return await create_order_from_cart(db, user_id, order_in)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


@router.get("/{user_id}", response_model=list[OrderOut])
async def list_orders(
    user_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if current_user.id != user_id and not current_user.is_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")
    # ⚡ Bolt: Prevent unnecessary eager loading of the User and Payment models since
    # they are not returned in OrderOut
    result = await db.scalars(
        select(Order)
        .where(Order.user_id == user_id)
        .options(noload(Order.user), noload(Order.payment))
    )
    return list(result)

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.db.session import get_db
from app.schemas.order import OrderCreate, OrderOut
from app.services.order_service import create_order_from_cart
from app.models.order import Order

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/{user_id}", response_model=OrderOut)
def create_order(user_id: UUID, order_in: OrderCreate, db: Session = Depends(get_db)):
    try:
        return create_order_from_cart(db, user_id, order_in)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{user_id}", response_model=list[OrderOut])
def list_orders(user_id: UUID, db: Session = Depends(get_db)):
    return db.query(Order).filter(Order.user_id == user_id).all()

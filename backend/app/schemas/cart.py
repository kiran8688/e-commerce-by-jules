from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class CartItemBase(BaseModel):
    product_id: UUID
    quantity: int

class CartItemCreate(CartItemBase):
    pass

class CartItemOut(CartItemBase):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    cart_id: UUID
    unit_price_snapshot: float
    added_at: datetime

class CartOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    user_id: UUID
    items: list[CartItemOut]
    created_at: datetime
    updated_at: datetime

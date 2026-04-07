from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, ConfigDict

class OrderItemOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    product_id: UUID
    product_name_snapshot: str
    sku_snapshot: str
    quantity: int
    unit_price_snapshot: float
    line_total: float

class OrderOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    order_number: str
    user_id: UUID
    status: str
    payment_status: str
    total_amount: float
    created_at: datetime
    items: list[OrderItemOut]

class OrderCreate(BaseModel):
    shipping_address_id: UUID
    billing_address_id: UUID | None = None
    notes: str | None = None

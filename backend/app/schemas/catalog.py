from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    name: str
    slug: str
    sku: str
    short_description: str | None = None
    description: str
    price: float
    compare_at_price: float | None = None
    currency: str = "USD"
    is_active: bool = True
    is_featured: bool = False

class ProductCreate(ProductBase):
    category_id: UUID

class ProductOut(ProductBase):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    category_id: UUID
    created_at: datetime
    updated_at: datetime

class CategoryBase(BaseModel):
    name: str
    slug: str
    description: str | None = None
    is_active: bool = True

class CategoryCreate(CategoryBase):
    parent_id: UUID | None = None

class CategoryOut(CategoryBase):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    parent_id: UUID | None
    created_at: datetime
    updated_at: datetime

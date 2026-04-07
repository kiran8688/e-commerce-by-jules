from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.catalog import Product, Category
from app.schemas.catalog import ProductCreate

def get_product(db: Session, product_id: UUID) -> Product | None:
    return db.scalar(select(Product).where(Product.id == product_id))

def get_products(db: Session, skip: int = 0, limit: int = 100) -> list[Product]:
    return list(db.scalars(select(Product).offset(skip).limit(limit)))

def create_product(db: Session, product: ProductCreate) -> Product:
    db_product = Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_categories(db: Session, skip: int = 0, limit: int = 100) -> list[Category]:
    return list(db.scalars(select(Category).offset(skip).limit(limit)))

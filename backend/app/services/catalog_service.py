from uuid import UUID

from app.models.catalog import Category, Product
from app.schemas.catalog import ProductCreate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import raiseload


async def get_product(db: AsyncSession, product_id: UUID) -> Product | None:
    return await db.scalar(select(Product).where(Product.id == product_id))

async def get_products(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[Product]:
    # Optimize by disabling eager loading of all relationships (e.g., category, images)
    # since the listing endpoints (like ProductOut) only require the scalar fields,
    # preventing N+1 or unnecessary secondary queries. raiseload fails loudly.
    result = await db.scalars(select(Product).options(raiseload("*")).offset(skip).limit(limit))
    return list(result)

async def create_product(db: AsyncSession, product: ProductCreate) -> Product:
    db_product = Product(**product.model_dump())
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product

async def get_categories(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[Category]:
    # Optimize by disabling eager loading of all relationships (e.g., products)
    # since the listing endpoints (like CategoryOut) only require the scalar fields.
    result = await db.scalars(select(Category).options(raiseload("*")).offset(skip).limit(limit))
    return list(result)

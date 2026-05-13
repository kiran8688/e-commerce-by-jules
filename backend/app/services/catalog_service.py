from uuid import UUID

from app.models.catalog import Category, Product
from app.schemas.catalog import ProductCreate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import raiseload


async def get_product(db: AsyncSession, product_id: UUID) -> Product | None:
    # Performance Optimization: Use raiseload('*') to prevent unnecessary default lazy='selectin' eager loading
    # of relationships (images, inventory, reviews, category) when fetching a product, as they are not needed by the output schema.
    return await db.scalar(select(Product).options(raiseload('*')).where(Product.id == product_id))

async def get_products(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[Product]:
    # Performance Optimization: Use raiseload('*') to prevent unnecessary default lazy='selectin' eager loading
    # of relationships (images, inventory, reviews, category) when fetching products, as they are not needed by the output schema.
    result = await db.scalars(select(Product).options(raiseload('*')).offset(skip).limit(limit))
    return list(result)

async def create_product(db: AsyncSession, product: ProductCreate) -> Product:
    db_product = Product(**product.model_dump())
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product

async def get_categories(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[Category]:
    # Performance Optimization: Use raiseload('*') to prevent unnecessary default lazy='selectin' eager loading
    # of relationships (products) when fetching categories, as they are not needed by the output schema.
    result = await db.scalars(select(Category).options(raiseload('*')).offset(skip).limit(limit))
    return list(result)

from uuid import UUID

from app.models.catalog import Category, Product
from app.schemas.catalog import ProductCreate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import noload


async def get_product(db: AsyncSession, product_id: UUID) -> Product | None:
    return await db.scalar(select(Product).where(Product.id == product_id))


async def get_products(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[Product]:
    # Performance Optimization:
    # Use .options(noload("*")) to prevent eager loading of relationships
    # (e.g. category, images, inventory, reviews which use lazy="selectin" by default)
    # as they are not needed in the basic list response schema (ProductOut), reducing N+1 queries.
    stmt = select(Product).options(noload("*")).offset(skip).limit(limit)
    result = await db.scalars(stmt)
    return list(result)


async def create_product(db: AsyncSession, product: ProductCreate) -> Product:
    db_product = Product(**product.model_dump())
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product


async def get_categories(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[Category]:
    # Performance Optimization:
    # Prevent eager loading of 'products' relationship which uses lazy="selectin".
    # Only return the base category data needed for the list endpoint.
    stmt = select(Category).options(noload("*")).offset(skip).limit(limit)
    result = await db.scalars(stmt)
    return list(result)

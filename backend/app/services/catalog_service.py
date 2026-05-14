from uuid import UUID

from app.models.catalog import Category, Product
from app.schemas.catalog import ProductCreate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import raiseload


async def get_product(db: AsyncSession, product_id: UUID) -> Product | None:
    # Performance Optimization: Prevent unnecessary eager loading of product relationships
    # (images, reviews, inventory, category) when fetching a single product.
    # This significantly reduces database latency and memory footprint since the output schema
    # does not include these relationships.
    return await db.scalar(select(Product).where(Product.id == product_id).options(raiseload('*')))

async def get_products(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[Product]:
    # Performance Optimization: Prevent unnecessary eager loading of product relationships
    # when fetching a list of products. This eliminates the N+1/over-fetching bottleneck.
    result = await db.scalars(select(Product).offset(skip).limit(limit).options(raiseload('*')))
    return list(result)

async def create_product(db: AsyncSession, product: ProductCreate) -> Product:
    db_product = Product(**product.model_dump())
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product

async def get_categories(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[Category]:
    # Performance Optimization: Prevent unnecessary eager loading of category relationships
    # (e.g., products) to avoid over-fetching when the output schema doesn't need them.
    result = await db.scalars(select(Category).offset(skip).limit(limit).options(raiseload('*')))
    return list(result)

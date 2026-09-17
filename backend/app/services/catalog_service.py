from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import noload
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.catalog import Product, Category
from app.schemas.catalog import ProductCreate

async def get_product(db: AsyncSession, product_id: UUID) -> Product | None:
    return await db.scalar(select(Product).where(Product.id == product_id))

async def get_products(db: AsyncSession, skip: int = 0, limit: int = 100, load_relationships: bool = True) -> list[Product]:
    stmt = select(Product).offset(skip).limit(limit)
    if not load_relationships:
        # Optimization: prevent eager loading of relationships when only base product data is needed
        stmt = stmt.options(noload('*'))
    result = await db.scalars(stmt)
    return list(result)

async def create_product(db: AsyncSession, product: ProductCreate) -> Product:
    db_product = Product(**product.model_dump())
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product

async def get_categories(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[Category]:
    result = await db.scalars(select(Category).offset(skip).limit(limit))
    return list(result)

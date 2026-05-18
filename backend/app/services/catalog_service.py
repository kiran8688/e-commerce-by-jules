from uuid import UUID

from app.models.catalog import Category, Product
from app.schemas.catalog import ProductCreate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import raiseload


async def get_product(db: AsyncSession, product_id: UUID) -> Product | None:
    return await db.scalar(select(Product).where(Product.id == product_id))

async def get_products(
    db: AsyncSession, skip: int = 0, limit: int = 100, load_options: list = None
) -> list[Product]:
    # Performance Optimization: Prevent N+1 queries from lazy="selectin" relationships
    # when relationship data is not needed. Pass load_options=[raiseload('*')] to skip.
    stmt = select(Product).offset(skip).limit(limit)
    if load_options:
        stmt = stmt.options(*load_options)
    result = await db.scalars(stmt)
    return list(result)

async def create_product(db: AsyncSession, product: ProductCreate) -> Product:
    db_product = Product(**product.model_dump())
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product

async def get_categories(
    db: AsyncSession, skip: int = 0, limit: int = 100, load_options: list = None
) -> list[Category]:
    # Performance Optimization: Prevent N+1 queries from lazy="selectin" relationships
    # when relationship data is not needed. Pass load_options=[raiseload('*')] to skip.
    stmt = select(Category).offset(skip).limit(limit)
    if load_options:
        stmt = stmt.options(*load_options)
    result = await db.scalars(stmt)
    return list(result)

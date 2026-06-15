from uuid import UUID
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.catalog import Product, Category
from app.schemas.catalog import ProductCreate

async def get_product(db: AsyncSession, product_id: UUID) -> Product | None:
    return await db.scalar(select(Product).where(Product.id == product_id))

async def get_products(db: AsyncSession, skip: int = 0, limit: int = 100, load_options: list | None = None) -> list[Product]:
    stmt = select(Product).offset(skip).limit(limit)
    # Performance optimization: Allow routers to pass load options (like raiseload)
    # to prevent unnecessary eager loading of relationships when they aren't needed.
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

async def get_categories(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[Category]:
    result = await db.scalars(select(Category).offset(skip).limit(limit))
    return list(result)

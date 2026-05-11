from uuid import UUID

from app.models.catalog import Category, Product
from app.schemas.catalog import ProductCreate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import raiseload


async def get_product(db: AsyncSession, product_id: UUID) -> Product | None:
    return await db.scalar(select(Product).where(Product.id == product_id))

async def get_products(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[Product]:
    # Use raiseload('*') to safely prevent unnecessary eager loading of relationships
    # (which are configured with lazy='selectin') when fetching lists, as the
    # ProductOut schema does not require them.
    result = await db.scalars(select(Product).options(raiseload('*')).offset(skip).limit(limit))
    return list(result)

async def create_product(db: AsyncSession, product: ProductCreate) -> Product:
    db_product = Product(**product.model_dump())
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product

async def get_categories(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[Category]:
    # Use raiseload('*') to safely prevent unnecessary eager loading of relationships
    # when fetching lists.
    result = await db.scalars(select(Category).options(raiseload('*')).offset(skip).limit(limit))
    return list(result)

from uuid import UUID

from app.models.catalog import Category, Product
from app.schemas.catalog import ProductCreate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import noload


async def get_product(db: AsyncSession, product_id: UUID) -> Product | None:
    return await db.scalar(select(Product).where(Product.id == product_id))


async def get_products(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[Product]:
    result = await db.scalars(select(Product).offset(skip).limit(limit))
    return list(result)


async def get_products_for_catalog_list(
    db: AsyncSession, skip: int = 0, limit: int = 100
) -> list[Product]:
    """
    ⚡ Bolt: Optimized query for ProductOut schema.
    Applies noload('*') to prevent eager loading of relationships
    (category, images, inventory, reviews)
    since they are not present in the ProductOut schema, saving N+1 unnecessary queries.
    """
    result = await db.scalars(select(Product).options(noload("*")).offset(skip).limit(limit))
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

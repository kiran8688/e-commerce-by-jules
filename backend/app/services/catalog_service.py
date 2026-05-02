from uuid import UUID

from app.models.catalog import Category, Product
from app.schemas.catalog import ProductCreate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import noload


async def get_product(db: AsyncSession, product_id: UUID) -> Product | None:
    return await db.scalar(select(Product).where(Product.id == product_id))

async def get_products(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[Product]:
    # Use noload to prevent eager loading of relationships (which default to selectin)
    # since the list endpoints return schemas that don't include these relationships.
    query = select(Product).options(
        noload(Product.category),
        noload(Product.images),
        noload(Product.inventory),
        noload(Product.reviews)
    ).offset(skip).limit(limit)
    result = await db.scalars(query)
    return list(result)

async def create_product(db: AsyncSession, product: ProductCreate) -> Product:
    db_product = Product(**product.model_dump())
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product

async def get_categories(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[Category]:
    # Use noload to prevent eager loading of relationships
    query = select(Category).options(noload(Category.products)).offset(skip).limit(limit)
    result = await db.scalars(query)
    return list(result)

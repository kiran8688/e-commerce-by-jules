from uuid import UUID

from app.models.catalog import Category, Product
from app.schemas.catalog import ProductCreate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import noload


async def get_product(db: AsyncSession, product_id: UUID) -> Product | None:
    return await db.scalar(select(Product).where(Product.id == product_id))

async def get_products(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[Product]:
    # Optimization: Use noload to prevent eager loading of relationships defined with
    # lazy="selectin" in the model since they are not needed for the list endpoint
    # (ProductOut schema). This prevents significant over-fetching.
    stmt = select(Product).options(
        noload(Product.category),
        noload(Product.images),
        noload(Product.inventory),
        noload(Product.reviews)
    ).offset(skip).limit(limit)
    result = await db.scalars(stmt)
    return list(result)

async def create_product(db: AsyncSession, product: ProductCreate) -> Product:
    db_product = Product(**product.model_dump())
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product

async def get_categories(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[Category]:
    # Optimization: Prevent eager loading of products relationship
    stmt = select(Category).options(noload(Category.products)).offset(skip).limit(limit)
    result = await db.scalars(stmt)
    return list(result)

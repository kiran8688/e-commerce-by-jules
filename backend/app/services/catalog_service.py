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
    # Use noload() for relationships to prevent eager loading (lazy='selectin' default).
    # Since these relationships are not included in the ProductOut schema,
    # fetching them causes unnecessary background queries and over-fetching.
    result = await db.scalars(
        select(Product)
        .options(
            noload(Product.category),
            noload(Product.images),
            noload(Product.inventory),
            noload(Product.reviews)
        )
        .offset(skip)
        .limit(limit)
    )
    return list(result)

async def create_product(db: AsyncSession, product: ProductCreate) -> Product:
    db_product = Product(**product.model_dump())
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product

async def get_categories(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[Category]:
    # Performance Optimization:
    # Use noload() to avoid loading the Category.products relationship since it's
    # not required in the CategoryOut schema, reducing query overhead.
    result = await db.scalars(
        select(Category)
        .options(noload(Category.products))
        .offset(skip)
        .limit(limit)
    )
    return list(result)

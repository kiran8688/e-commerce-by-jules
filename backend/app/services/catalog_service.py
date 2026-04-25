from uuid import UUID

from app.models.catalog import Category, Product
from app.schemas.catalog import ProductCreate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import noload


async def get_product(db: AsyncSession, product_id: UUID) -> Product | None:
    return await db.scalar(select(Product).where(Product.id == product_id))


async def get_products(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[Product]:
    # Optimization: Prevent over-fetching of eager-loaded relationships
    # The ProductOut schema only requires base fields, so we do not need to
    # fetch related objects like category, images, inventory, or reviews.
    result = await db.scalars(
        select(Product)
        .options(
            noload(Product.category),
            noload(Product.images),
            noload(Product.inventory),
            noload(Product.reviews),
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
    # Optimization: Prevent over-fetching of the products relationship
    result = await db.scalars(
        select(Category).options(noload(Category.products)).offset(skip).limit(limit)
    )
    return list(result)

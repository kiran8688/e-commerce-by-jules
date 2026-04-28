from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import noload
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.catalog import Product, Category
from app.schemas.catalog import ProductCreate

async def get_product(db: AsyncSession, product_id: UUID) -> Product | None:
    return await db.scalar(select(Product).where(Product.id == product_id))

async def get_products(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[Product]:
    # ⚡ Bolt: Use noload() to prevent N+1 over-fetching of relationships on list endpoints
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
    # ⚡ Bolt: Use noload() to prevent N+1 over-fetching of relationships on list endpoints
    query = select(Category).options(noload(Category.products)).offset(skip).limit(limit)
    result = await db.scalars(query)
    return list(result)

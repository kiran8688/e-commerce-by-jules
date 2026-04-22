from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import noload
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.catalog import Product, Category
from app.schemas.catalog import ProductCreate

async def get_product(db: AsyncSession, product_id: UUID) -> Product | None:
    return await db.scalar(select(Product).where(Product.id == product_id))

async def get_products(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[Product]:
    # Use noload to prevent N+1 eager loading of relationships that are not
    # included in the ProductOut schema. This reduces database queries and memory usage.
    query = select(Product).offset(skip).limit(limit).options(
        noload(Product.category),
        noload(Product.images),
        noload(Product.inventory),
        noload(Product.reviews)
    )
    result = await db.scalars(query)
    return list(result)

async def create_product(db: AsyncSession, product: ProductCreate) -> Product:
    db_product = Product(**product.model_dump())
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product

async def get_categories(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[Category]:
    # Use noload to prevent fetching products when only listing categories
    query = select(Category).offset(skip).limit(limit).options(
        noload(Category.products)
    )
    result = await db.scalars(query)
    return list(result)

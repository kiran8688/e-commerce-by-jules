from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import raiseload
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.catalog import Product, Category
from app.schemas.catalog import ProductCreate

async def get_product(db: AsyncSession, product_id: UUID) -> Product | None:
    return await db.scalar(select(Product).where(Product.id == product_id))

async def get_products(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[Product]:
    # Performance Optimization:
    # Adding `.options(raiseload('*'))` prevents the default `lazy="selectin"`
    # from executing multiple unnecessary background queries (e.g. for images, inventory, reviews)
    # since the Pydantic schemas (ProductOut) only require scalar columns.
    # This saves ~4 database queries per API call and avoids unnecessary object hydration.
    result = await db.scalars(select(Product).options(raiseload('*')).offset(skip).limit(limit))
    return list(result)

async def create_product(db: AsyncSession, product: ProductCreate) -> Product:
    db_product = Product(**product.model_dump())
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product

async def get_categories(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[Category]:
    # Performance Optimization:
    # Prevent default selectin eager load on `products` relationship when listing categories.
    result = await db.scalars(select(Category).options(raiseload('*')).offset(skip).limit(limit))
    return list(result)

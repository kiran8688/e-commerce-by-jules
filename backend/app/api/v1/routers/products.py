from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import noload

from app.db.session import get_db
from app.schemas.catalog import ProductOut
from app.services.catalog_service import get_products

router = APIRouter(prefix="/products", tags=["Catalog"])

@router.get("/", response_model=list[ProductOut])
async def read_products(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    # ⚡ Bolt Optimization: Prevent N+1 queries from lazy='selectin' relationships that are omitted from ProductOut by using noload('*')
    return await get_products(db, skip=skip, limit=limit, load_options=[noload("*")])

from app.db.session import get_db
from app.schemas.catalog import ProductOut
from app.services.catalog_service import get_products
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import raiseload

router = APIRouter(prefix="/products", tags=["Catalog"])

@router.get("/", response_model=list[ProductOut])
async def read_products(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    # ⚡ Bolt: Prevent unnecessary eager loading of relationships
    # since they aren't included in ProductOut.
    return await get_products(db, skip=skip, limit=limit, load_options=[raiseload("*")])

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.catalog import ProductOut
from app.services.catalog_service import get_products

router = APIRouter(prefix="/products", tags=["Catalog"])

@router.get("/", response_model=list[ProductOut])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_products(db, skip=skip, limit=limit)

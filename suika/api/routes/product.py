from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from suika.core.db import get_db
from suika.models.product import Product
from suika.schemas.product import Product as ProductSchema

router = APIRouter()


@router.get("/", response_model=List[ProductSchema])
async def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()


@router.get("/{product_id}", response_model=ProductSchema)
async def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found.")

    return product

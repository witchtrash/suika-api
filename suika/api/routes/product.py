from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from suika.core.db import get_db
from suika.models.product import Product
from suika.schemas.product import Product as ProductSchema
from suika.schemas.price import Price as PriceSchema

router = APIRouter()


@router.get(
    "/",
    response_model=List[ProductSchema],
    summary="Get products",
    response_description="Response containing a list of products",
)
async def get_products(db: Session = Depends(get_db)):
    """
    Get a list of products
    """
    return db.query(Product).all()


@router.get(
    "/{product_id}",
    response_model=ProductSchema,
    summary="Get product",
    response_description="Response containing a single product",
)
async def get_product(product_id: int, db: Session = Depends(get_db)):
    """
    Get a single product by ID
    """
    product = db.query(Product).filter(Product.id == product_id).first()

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found.")

    return product


@router.get(
    "/{product_id}/price",
    response_model=List[PriceSchema],
    summary="Get prices",
    response_description="Response containing historical "
    "pricing information for a given product",
)
async def get_prices(product_id: int, db: Session = Depends(get_db)):
    """
    Get pricing history for a product",
    """
    product = db.query(Product).filter(Product.id == product_id).first()

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found.")

    return product.prices

from typing import List, Optional, Literal
from fastapi import APIRouter, Depends, HTTPException
from pydantic.main import BaseModel
from sqlalchemy.orm import Session
from fastapi_pagination import Page, paginate
from sqlalchemy.sql.expression import asc, desc

from suika.core.db import get_db
from suika.models.product import Product
from suika.models.price import Price
from suika.schemas.product import ProductResponse
from suika.schemas.price import PriceResponse

router = APIRouter()


class ProductParams(BaseModel):
    sort_direction: Optional[Literal["asc", "desc"]]
    sort_by: Optional[Literal["id", "name", "price"]]
    filter: Optional[str]


@router.get(
    "/",
    response_model=Page[ProductResponse],
    summary="Get products",
    response_description="Response containing a list of products",
)
async def get_products(
    db: Session = Depends(get_db), params: ProductParams = Depends()
):
    """
    Get a list of products
    """

    query = db.query(Product).join(Price)
    direction = asc if params.sort_direction == 'asc' else desc

    match params.sort_by:
        case 'name':
            query = query.order_by(direction(Product.name))
        case 'price':
            query = query.order_by(direction(Price.price))
        case _:
            query = query.order_by(direction(Product.id))

    return paginate(query.all())


@router.get(
    "/{product_id}",
    response_model=ProductResponse,
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
    response_model=List[PriceResponse],
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

from math import ceil
from typing import List, Optional, Literal
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, conint
from sqlalchemy.orm import Session
from fastapi_pagination import Page, paginate
from sqlalchemy.sql.expression import asc, desc

from suika.core.db import get_db
from suika.models.product import Product
from suika.schemas.product import ProductResponse
from suika.schemas.price import PriceResponse
from suika.schemas.collection import Collection

router = APIRouter()


class ProductParams(BaseModel):
    sort_direction: Optional[Literal["asc", "desc"]]
    sort_by: Optional[Literal["id", "name", "current_price", "abv"]]
    filter: Optional[str]


class PaginationParams(BaseModel):
    page: conint(ge=1) = 1
    per_page: conint(ge=10, le=100) = 50


@router.get(
    "/",
    response_model=Collection[ProductResponse],
    summary="Get products",
    response_description="Response containing a list of products",
)
async def get_products(
    db: Session = Depends(get_db),
    params: ProductParams = Depends(),
    pagination: PaginationParams = Depends(),
):
    """
    Get a list of products
    """

    sort_field = params.sort_by if params.sort_by is not None else "id"
    sort = desc(sort_field) if params.sort_direction == "desc" else asc(sort_field)

    total = db.query(Product).count()
    page_count = ceil(total / pagination.per_page)
    offset = (pagination.page - 1) * pagination.per_page

    query = db.query(Product).order_by(sort).offset(offset).limit(pagination.per_page)

    return {
        "items": query.all(),
        "total": total,
        "current_page": pagination.page,
        "last_page": page_count,
        "per_page": pagination.per_page,
    }


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
    Get pricing history for a product
    """
    product = db.query(Product).filter(Product.id == product_id).first()

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found.")

    return product.prices

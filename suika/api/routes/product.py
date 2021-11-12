from typing import List, Optional, Literal
from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import asc, desc
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate

from suika.core.db import get_db
from suika.models.product import Product
from suika.schemas.product import ProductResponse
from suika.schemas.price import PriceResponse

router = APIRouter()


class ProductParams(BaseModel):
    sort_direction: Optional[Literal["asc", "desc"]] = Query("asc")
    sort_by: Optional[Literal["id", "name", "current_price", "abv"]] = Query("id")
    filter: Optional[str] = Query(None)


@router.get(
    "/",
    response_model=Page[ProductResponse],
    summary="Get products",
    response_description="Response containing a list of products",
)
async def get_products(
    db: Session = Depends(get_db),
    params: ProductParams = Depends(),
) -> Page[ProductResponse]:
    """
    Get a list of products
    """

    sort_field = params.sort_by if params.sort_by is not None else "id"
    sort = desc(sort_field) if params.sort_direction == "desc" else asc(sort_field)

    query = db.query(Product).order_by(sort)

    if params.filter:
        query = query.filter(
            Product.name.like(f"%{params.filter}%")
            | Product.sku.like(f"%{params.filter}")
        )

    return paginate(query)


@router.get(
    "/{product_id}",
    response_model=ProductResponse,
    summary="Get product",
    response_description="Response containing a single product",
)
async def get_product(
    product_id: int,
    db: Session = Depends(get_db),
) -> ProductResponse:
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
async def get_prices(
    product_id: int,
    db: Session = Depends(get_db),
) -> List[PriceResponse]:
    """
    Get pricing history for a product
    """
    product = db.query(Product).filter(Product.id == product_id).first()

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found.")

    return product.prices

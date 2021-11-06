from typing import Optional
from pydantic import BaseModel
from suika.schemas.common import Common
from suika.schemas.price import PriceResponse


class ProductBase(BaseModel):
    sku: str
    name: str
    volume: float
    abv: float
    country_of_origin: str
    available: bool
    container_type: str
    style: str
    sub_style: str
    producer: str
    short_description: str
    season: str


class ProductResponse(ProductBase, Common):
    id: str
    price: Optional[PriceResponse]

    class Config:
        orm_mode = True


class ProductRequest(ProductBase):
    class Config:
        orm_mode = True

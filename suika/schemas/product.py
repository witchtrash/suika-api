from suika.schemas.common import Common
from suika.schemas.price import Price


class Product(Common):
    id: str
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
    price: Price

    class Config:
        orm_mode = True

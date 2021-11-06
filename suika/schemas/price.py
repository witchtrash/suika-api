from suika.schemas.common import Common


class PriceResponse(Common):
    price: int

    class Config:
        orm_mode = True

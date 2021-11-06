from suika.schemas.common import Common


class Price(Common):
    price: int

    class Config:
        orm_mode = True

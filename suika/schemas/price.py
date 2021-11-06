from pydantic.main import BaseModel
from suika.schemas.common import Common


class PriceBase(BaseModel):
    price: int


class PriceResponse(PriceBase, Common):
    class Config:
        orm_mode = True


class PriceRequest(PriceBase):
    class Config:
        orm_mode = True

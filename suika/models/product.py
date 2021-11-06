from sqlalchemy import Column, Integer, String, Float, Boolean, Text
from sqlalchemy.orm import relationship
from suika.models.common import Common
from suika.models.price import Price


class Product(Common):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, autoincrement=True)
    sku = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    volume = Column(Float, nullable=False)
    abv = Column(Float, nullable=False)
    country_of_origin = Column(String, nullable=False)
    available = Column(Boolean, nullable=False)
    container_type = Column(String, nullable=False)
    style = Column(String, nullable=False)
    sub_style = Column(String, nullable=False)
    producer = Column(String, nullable=False)
    short_description = Column(Text)
    season = Column(String, nullable=False)
    prices = relationship("Price", back_populates="product")

    @property
    def price(self) -> Price | None:
        if len(self.prices) > 0:
            return self.prices[-1]
        return None

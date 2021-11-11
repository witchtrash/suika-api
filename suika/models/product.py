from sqlalchemy import Column, Integer, String, Float, Boolean, Text
from sqlalchemy.orm import relationship
from suika.models.common import Common


class Product(Common):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, autoincrement=True)
    sku = Column(String, unique=True, nullable=False, index=True)
    name = Column(String, nullable=False, index=True)
    volume = Column(Float, nullable=False)
    abv = Column(Float, nullable=False, index=True)
    country_of_origin = Column(String, nullable=False)
    available = Column(Boolean, nullable=False)
    container_type = Column(String, nullable=False)
    style = Column(String, nullable=False)
    sub_style = Column(String, nullable=False)
    producer = Column(String, nullable=False)
    short_description = Column(Text)
    season = Column(String, nullable=False)
    current_price = Column(Integer, nullable=True, index=True)
    prices = relationship("Price", back_populates="product")

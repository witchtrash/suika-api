from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from suika.models.common import Common


class Price(Common):
    __tablename__ = "price"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("product.id"), nullable=False)
    product = relationship("Product", back_populates="prices")
    price = Column(Integer, nullable=False)

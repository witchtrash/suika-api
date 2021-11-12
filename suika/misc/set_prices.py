from suika.core.db import SessionLocal
from suika.models.product import Product
from suika.models.price import Price

db = SessionLocal()

products = db.query(Product).join(Price).all()

for product in products:
    # Get the latest price for the product
    current_price = product.prices[-1]
    product.current_price = current_price.price

db.commit()

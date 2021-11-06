from fastapi import APIRouter
from suika.api.routes import index
from suika.api.routes import product

api_router = APIRouter()
api_router.include_router(index.router, tags=["suika"])
api_router.include_router(product.router, tags=["product"], prefix="/product")

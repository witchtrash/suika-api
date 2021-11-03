from fastapi import APIRouter
from suika.api.routes import index

api_router = APIRouter()
api_router.include_router(index.router, tags=["suika"])

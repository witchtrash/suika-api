__version__ = "0.1.0"

from fastapi import FastAPI
from fastapi_pagination import add_pagination

from suika.api.api import api_router

app = FastAPI(title="suika")
app.include_router(api_router)
add_pagination(app)

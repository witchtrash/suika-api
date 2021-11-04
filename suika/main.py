__version__ = "0.1.0"

from fastapi import FastAPI
from suika.api.api import api_router

app = FastAPI(title="suika")

app.include_router(api_router)

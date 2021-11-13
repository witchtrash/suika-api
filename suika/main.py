__version__ = "0.2.0"

from fastapi import FastAPI
from fastapi_pagination import add_pagination

from suika.api.api import api_router

app = FastAPI(
    title="suika",
    description="API for historical pricing information for "
    "the State Alcohol and Tobacco Company of Iceland ",
    license_info={
        "name": "MIT",
        "url": "https://github.com/witchtrash/suika-api/blob/main/LICENSE",
    },
    version=__version__,
)
app.include_router(api_router)
add_pagination(app)

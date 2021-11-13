from typing import TypeVar, Generic
from fastapi_pagination.default import Page
from pydantic import BaseModel
from datetime import datetime


class Common(BaseModel):
    date_created: datetime
    date_modified: datetime


T = TypeVar("T")


class Collection(Page[T], Generic[T]):
    class Config:
        allow_population_by_field_name = True
        fields = {"items": {"alias": "data"}}

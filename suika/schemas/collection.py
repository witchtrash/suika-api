from typing import List, TypeVar, Generic
from pydantic import BaseModel

T = TypeVar("T")


class Collection(BaseModel, Generic[T]):
    items: List[T]
    total: int
    per_page: int
    current_page: int
    last_page: int

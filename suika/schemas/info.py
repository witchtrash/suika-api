from pydantic import BaseModel


class Info(BaseModel):
    name: str
    version: str

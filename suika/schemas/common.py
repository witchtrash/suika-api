from pydantic import BaseModel
from datetime import datetime


class Common(BaseModel):
    date_created: datetime
    date_modified: datetime

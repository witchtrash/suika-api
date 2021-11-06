from sqlalchemy import Column, DateTime
from sqlalchemy.sql.functions import func
from suika.core.db import Base


class Common(Base):
    __abstract__ = True

    date_created = Column(
        DateTime,
        server_default=func.now(),
        nullable=False,
    )
    date_modified = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

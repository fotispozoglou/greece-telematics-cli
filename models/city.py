from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import mapped_column, Mapped

import uuid

from models.base import Base

class City( Base ):

    __tablename__ = "city"

    id: Mapped[str] = mapped_column(primary_key=True)
    name : Mapped[str]
    code : Mapped[str]

    def __init__( self, name, code ):

        self.id = str(uuid.uuid4())
        self.name = name
        self.code = code

    def __repr__( self ):

        return f"{ self.alias } ({ self.code })"
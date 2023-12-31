from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import mapped_column, Mapped

import uuid

from models.base import Base

class Station( Base ):

    __tablename__ = "station"

    id: Mapped[str] = mapped_column(primary_key=True)
    name : Mapped[str]
    alias : Mapped[str]
    code : Mapped[str]
    latitude : Mapped[str]
    longitude : Mapped[str]

    def __init__( self, name, alias, code, latitude, longitude ):

        self.id = str(uuid.uuid4())
        self.name = name
        self.alias = alias
        self.code = code
        self.latitude = latitude
        self.longitude = longitude

    def __repr__( self ):

        return f"{ self.alias } ({ self.code })"
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import mapped_column
import uuid

from models.base import Base

class Station( Base ):

    __tablename__ = "station"

    id: Column("id", String, primary_key=True)
    name: Column("name", String)
    alias: Column("alias", String)
    code: Column("code", String)
    latitude: Column("latitude", String)
    longitude: Column("longitude", String)

    def __init__( self, name, alias, code, latitude, longitude ):

        self.id = uuid.uuid4()
        self.name = name
        self.alias = alias
        self.code = code
        self.latitude = latitude
        self.longitude = longitude

    def __repr__( self ):

        return f"{ self.alias } ({ self.code })"
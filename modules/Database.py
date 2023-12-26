from sqlalchemy import create_engine, select
from sqlalchemy.orm import create_session, sessionmaker, Session

from models.base import Base

from models.station import Station

class Database:

    def __init__( self ):

        self.engine = create_engine("sqlite:///database/telematics.db")

        Base.metadata.create_all( bind=self.engine )

        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def get_all( self, Model, filter_by = None ):

        statement = select( Model )

        return self.session.scalars(statement).all()

    def insert( self, obj ):

        self.session.add( obj )

        self.session.commit()

database = Database()
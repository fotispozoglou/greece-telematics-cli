from sqlalchemy import create_engine
from sqlalchemy.orm import create_session, sessionmaker

from models.base import Base

class Database:

    def __init__( self ):

        self.engine = create_engine("sqlite:///database/telematics.db")

        Base.metadata.create_all( bind=self.engine )

        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        
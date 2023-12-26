import logging, uuid

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

class Logger:

    def __init__(self, name, log_file, level=logging.DEBUG ):
        
        self.sessionID = uuid.uuid4()
        self.handler = logging.FileHandler(log_file)        
        self.handler.setFormatter(formatter)

        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.logger.addHandler(self.handler)
        self.logger.info(f"Session { self.sessionID } started")
    
    def log_close( self ):

        self.info(f"Session { self.sessionID } stopped")

    def debug( self, message ):

        self.logger.debug( message )

    def info( self, message ):

        self.logger.info( message )

    def warning( self, message ):

        self.logger.warning( message )

    def error( self, message ):

        self.logger.error( message )

    def exception( self, message ):

        self.info(f"Session id { self.sessionID }")
        self.logger.exception( message )

logger = Logger('main_logger', 'logs/logs.log')
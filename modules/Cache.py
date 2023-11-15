cache = {}

class Cache:

    def __init__( self ):

        cache = {}

    def add( self, key, value ):

        cache[ key ] = value

    def get( self, key ):

        if key in self.cache:

            return cache[ key ]
        
        return None
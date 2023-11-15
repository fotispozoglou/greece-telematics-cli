import json
from requests import Session as RequestsSession

from modules.Cache import Cache

class Session:

    def __init__(self):

        self.session = RequestsSession()

    def set_header( self, name, value ):

        self.session.headers[ name ] = value

    def cache_middleware( self, url, response, cache = True ):

        content_type = response.headers.get('content-type')

        cached_response = {
            "status": response.status_code,
            "data": converters[ content_type ]( response.text ) if content_type in converters else None
        }

        Cache.add( url, cached_response )

        return Cache.get( url )
    
    def get( self, url, cache = True ):

        if cache and Cache.has( url ):

            return Cache.get( url )

        response = self.session.get( url )

        return self.cache_middleware( url, response, cache )


converters = {
    'text/html': lambda d : d,
    'application/json': lambda d : json.loads( d )
}
from enum import Enum

cache = {}

class Cache:

    @staticmethod
    def add( key, value ):

        cache[ key ] = value

    @staticmethod
    def get( key ):

        if key in cache:

            return cache[ key ]
        
        return None
    
    @staticmethod
    def has( key ):

        return key in cache
    
class Keys:
    STATION = "STN"
    CITY = "CT"
    ALL_CITIES = "ACTS"
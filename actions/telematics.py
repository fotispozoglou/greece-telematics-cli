from modules.Telematics import telematics
from modules.Console import Console

def list_cities( name ):

    all_cities = telematics.get_all_cities()

    for city in all_cities:

        Console.info( city )

def set_city( name ):

    telematics.set_city_name( name )

    telematics.set_api_token(  )
    telematics.set_city_code(  )

    stations = telematics.get_cities_stations()

    for station in stations:

        Console.info( station['name'] )
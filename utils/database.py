from modules.Database import database
from modules.Cache import Cache, Keys

def add_db_station( station ):

    database.insert_data("stations", {
        "id": station['id'],
        "name": station['name'],
        "code": station['code'],
        "latitude": station['latitude'],
        "longitude": station['longitude'],
        "pinned": 0,
    })

    key = f"{ Keys.STATION }{ station['id'] }"

    Cache.add( key, station )

def get_db_station( station_id ):

    key = f"{ Keys.STATION }{ station_id }"

    if Cache.has( key ):

        return Cache.get( key )
    
    station = database.query_data(f"SELECT * FROM stations WHERE id='{ station_id }'")

    return station

def set_db_last_city( city_name ):

    database.update_data("preferences", {
        "last_city": city_name
    }, 'id="preferences"')

def get_db_preferences():

    preferences = database.query_data("SELECT * FROM preferences")

    return preferences

def initialize_preferences_table():

    preferences = database.query_data("SELECT * FROM preferences")

    if len( preferences ) <= 0:

        database.raw("INSERT INTO preferences ( id, last_city, last_station ) VALUES ( 'preferences', '', '' )")
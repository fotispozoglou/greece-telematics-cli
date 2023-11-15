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
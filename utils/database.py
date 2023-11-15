from modules.Database import database

def add_station( station ):

    database.insert_data("stations", {
        "id": station['id'],
        "name": station['name'],
        "code": station['code'],
        "latitude": station['latitude'],
        "longitude": station['longitude'],
        "pinned": 0,
    })


StationModel = {
    "id": "INTEGER PRIMARY KEY",
    "name": "TEXT",
    "code": "TEXT",
    "latitude": "TEXT",
    "longitude": "TEXT",
    "pinned": "INT"
}

CityModel = {
    "id": "INTEGER PRIMARY KEY",
    "name": "TEXT",
    "uri": "TEXT",
}

PreferencesModel = {
    "id": "TEXT",
    "last_city": "TEXT",
    "last_station": "TEXT",
}
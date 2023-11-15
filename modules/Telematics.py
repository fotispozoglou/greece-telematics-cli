import requests, re, json
from modules.Console import Console

BASE = "https://{}.citybus.gr/el/stops"
STATION_VEHICLES_URI = "https://rest.citybus.gr/api/v1/el/{}/stops/live/{}"
STATION_DATA_URI = "https://rest.citybus.gr/api/v1/el/{}/stops/{}"

class Telematics:

    def __init__( self ):

        self.session = requests.Session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0",
            "Content-Type": "application/json; charset=utf-8"
        }

    def set_api_token( self ):

        response = self.session.get( BASE )

        token = re.search(r"token = '(.*)'", response.text).group(1)

        self.session.headers['Authorization'] = f"Bearer { token }"

    def get_station_vehicles( self, station_code ):

        try:

            response = self.session.get( STATION_VEHICLES_URI.format( station_code ) )

            data = json.loads( response.text )

            vehicles = data['vehicles']

            return vehicles

        except Exception as e:

            Console.error(f"{ e }", "get_station_vehicle")

    def get_station_data( self, code ):

        try:

            response = self.session.get( STATION_DATA_URI.format( code ) )

            data = json.loads( response.text )

            return data
        
        except Exception as e:

            raise e
            
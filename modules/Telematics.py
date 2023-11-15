import requests, re, json
from bs4 import BeautifulSoup

from modules.Console import Console
from modules.Cache import Cache, Keys
from utils.regex import city_url_regex

BASE = "https://citybus.gr/"
CITY_BASE = "https://{}.citybus.gr/el/stops"
STATION_VEHICLES_URI = "https://rest.citybus.gr/api/v1/el/{}/stops/live/{}"
STATION_DATA_URI = "https://rest.citybus.gr/api/v1/el/{}/stops/{}"
CITY_STATIONS_URI = "https://rest.citybus.gr/api/v1/el/{}/stops"

class Telematics:

    def __init__( self ):

        self.session = requests.Session()
        self.city_name = None
        self.city_code = None
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0",
            "Content-Type": "application/json; charset=utf-8"
        }

    def set_city_name( self, city_name ):

        self.city_name = city_name

    def set_api_token( self ):

        if self.city_name == None:

            return Console.error("Please select a city")

        response = self.session.get( CITY_BASE.format( self.city_name ) )

        token = re.search(r"token = '(.*)'", response.text).group(1)

        self.session.headers['Authorization'] = f"Bearer { token }"

    def set_city_code( self ):

        if self.city_name == None:

            return Console.error("Please select a city")

        response = self.session.get( CITY_BASE.format( self.city_name ) )

        code = re.search(r"agencyCode = (.*);", response.text).group(1)

        self.city_code = code


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
            
    def get_all_cities( self ):

        try:

            if Cache.has( Keys.ALL_CITIES ):

                return Cache.get( Keys.ALL_CITIES )
            
            response = self.session.get( BASE )

            soup = BeautifulSoup( response.text, features='lxml' )

            cities_links_elements = soup.find_all("a", { 'class': ['btn', 'btn-primary', 'text-nowrap'] })
        
            cities = []

            for cities_links_element in cities_links_elements:

                city = city_url_regex.findall( cities_links_element['href'] )

                cities.append( city[0] )

            Cache.add(f"{ Keys.ALL_CITIES }", cities)

            return cities

        except Exception as e:

            raise e
            
    def get_cities_stations( self ):

        try:

            key = f"{ Keys.ALL_STATIONS }{ self.city_code }"

            if Cache.has( key ):

                return Cache.get( key )
                                    
            response = self.session.get( CITY_STATIONS_URI.format( self.city_code ) )

            print(response.headers.get('content-type'))

            input()

            data = json.loads( response.text )

            Cache.add( key, data )

            return data
        
        except Exception as e:

            raise e
        

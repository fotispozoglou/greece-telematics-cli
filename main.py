import traceback

from modules.Console import Console
from modules.Telematics import Telematics
from modules.Database import database
from modules.Menu import Menu, MenuOption
from modules.KeyboardEvent import KeyboardEvent
from modules.Logger import Logger
from modules.Session import Session

from utils.database import initialize_preferences_table, get_db_preferences, set_db_last_city

from models.models import StationModel, PreferencesModel

live_tracking = False

def handle_change_city():

    cities = telematics.get_all_cities()

    for index, city in enumerate(cities):

        Menu.print_option( index + 1, city )

    city_index = int(Menu.input("enter city number"))

    select_city_name = cities[ city_index - 1 ]

    telematics.set_city_name( select_city_name )

    telematics.set_city_code(  )

    set_db_last_city( select_city_name )

def handle_change_station():

    stations = telematics.get_cities_stations()

    for index, station in enumerate(stations):

        Menu.print_option( index + 1, station['name'] )

    station_index = int(Menu.input("enter station number"))

def menu():

    # session = Session()

    # session.get( 'https://alexandroupoli.citybus.gr/el/stops' )

    # input()

    Console.clear()

    Menu.print_menu_config("CITY    |", telematics.city_name)
    Menu.print_menu_config("STATION |", telematics.city_name)
    Menu.print_menu_seperator( 50 )

    Menu.menu((
        ("Change City", handle_change_city),
        ("Change Station", handle_change_station),
    ))

    menu()

if __name__ == "__main__":

    try:

        logger = Logger('main_logger', 'logs/logs.log')

        logger.info("Program Started")

        telematics = Telematics()

        database.connect()

        database.create_table("stations", StationModel)
        database.create_table("preferences", PreferencesModel)

        initialize_preferences_table()

        preferences = get_db_preferences()

        city_name = preferences[0][1]

        telematics.set_city_name( city_name )

        telematics.set_city_code(  )

        telematics.set_api_token(  )

        logger.info("Initialization Completed")

        menu()

    except Exception as e:

        if e is not None:

            logger.exception( e )

            print(traceback.format_exc())

        else:
            
            Console.error("Unexpected Error")

            logger.error("Unexpected Error")

    finally:

        logger.info("Program Ended")

# enter_press_event = KeyboardEvent([ keyboard.Key.enter ], disable_live_tracking)

# enter_press_event.start()
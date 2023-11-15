import traceback

from modules.Console import Console
from modules.Telematics import Telematics
from modules.Database import database
from modules.Menu import Menu, MenuOption
from modules.KeyboardEvent import KeyboardEvent
from modules.Logger import Logger

from utils.regex import city_url_regex

from models.models import StationModel

live_tracking = False

def handle_change_city():

    cities = telemetics.get_all_cities()

    for index, city in enumerate(cities):

        Menu.print_option( index + 1, city )

    city_index = int(Menu.input("enter city number"))

    telemetics.set_city_name( cities[ city_index - 1 ] )

def menu():

    Console.clear()

    Menu.print_menu_config("CITY    |", telemetics.city_name)
    Menu.print_menu_config("STATION |", telemetics.city_name)
    Menu.print_menu_seperator( 50 )

    Menu.menu((
        ("Change City", handle_change_city),
    ))

    menu()

if __name__ == "__main__":

    try:

        logger = Logger('main_logger', 'logs/logs.log')

        logger.info("Program Started")

        telemetics = Telematics()

        database.connect()

        database.create_table("stations", StationModel)

        telemetics.set_api_token()

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
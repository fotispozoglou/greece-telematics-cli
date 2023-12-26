import traceback, asyncio, time, threading, os

from modules.Console import Console
from modules.Menu import Menu
from modules.Command import Command
from modules.Option import Option

from modules.Telematics import telematics
from modules.Database import database
from modules.Logger import logger

from models.station import Station

from actions.telematics import list_cities, set_city

def print_help():

    print("""Available commands:

Status commands:
city              : Print's selected city.
station           : Print's selected station.
live              : Track next bus of current station.

Action commands:
add station ( code ) : Add a station by code ( code can be found on the official telematics site ).
set city ( name )    : Change the selected city.
change station       : Change the selected station.
list cities          : List all cities
list city stations   : List all stations of city""")

def clear_screen():

    os.system("clear")

def start_menu():

    Console.clear()

    asyncio.run(menu.start_menu_routine())

if __name__ == "__main__":

    menu = Menu()
    
    try:

        logger.info("Program Started")

        logger.info("Initialization Completed")

        help_command = Command("help", print_help)
        clear_command = Command("clear", clear_screen)

        add_city_command = Command("list cities", list_cities)
        set_city_command = Command("set city", set_city)

        menu.register( help_command )
        menu.register( clear_command )
        menu.register( add_city_command )
        menu.register( set_city_command )

        start_menu()

    except Exception as e:

        if e is not None:

            logger.exception( e )

            print(traceback.format_exc())

        else:
            
            Console.error("Unexpected Error")

            logger.error("Unexpected Error")

    finally:

        logger.info("Program Ended")



# if os.path.exists("database") == False:

#         os.mkdir("database")
#         open('database/telematics.db', 'w').close() 

#     if os.path.exists("logs") == False:

#         os.mkdir("logs")
#         open('logs/logs.log', 'w').close() 
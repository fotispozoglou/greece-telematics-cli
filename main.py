import traceback, asyncio, time, threading, os

from modules.Console import Console
from modules.Telematics import Telematics
from modules.Database import Database
from modules.Logger import Logger
from modules.Menu import Menu
from modules.Command import Command
from modules.Option import Option

def print_help():

    print("""Available commands:

Status commands:
city              : Print's selected city.
station           : Print's selected station.
live              : Track next bus of current station.

Action commands:
add city ( name )    : Add a city by name.
add station ( code ) : Add a station by code ( code can be found on the official telematics site ).
change city          : Change the select city.
change station       : Change the selected station.""")

def clear_screen():

    os.system("clear")

def start_menu():

    Console.clear()

    asyncio.run(menu.start_menu_routine())

if __name__ == "__main__":

    logger = Logger('main_logger', 'logs/logs.log')
    menu = Menu()
    
    try:

        logger.info("Program Started")

        telematics = Telematics()

        database = Database()

        logger.info("Initialization Completed")

        help_command = Command("help", print_help)
        clear_command = Command("clear", clear_screen)

        menu.register( help_command )
        menu.register( clear_command )

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
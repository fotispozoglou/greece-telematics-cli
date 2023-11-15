import traceback

from modules.Console import Console
from modules.Telematics import Telematics
from modules.Database import database
from modules.Menu import Menu
from modules.KeyboardEvent import KeyboardEvent
from utils.database import add_station

from models.models import StationModel

live_tracking = False

def handle_add_station():

    code = Menu.input('enter station code')

    station = telemetics.get_station_data( code )

    if 'id' not in station:

        return
    
    add_station( station )

def handle_show_stations():

    pass

def handle_live_tracking():

    pass

def menu():

    Console.clear()

    Menu.menu((
        ("Add Station", handle_add_station),
        ("Show Added Stations", handle_show_stations),
        ("Live Tracking", handle_live_tracking)
    ))

    menu()

if __name__ == "__main__":

    try:

        telemetics = Telematics()

        database.connect()

        database.create_table("stations", StationModel)

        telemetics.set_api_token()

        menu()

    except Exception as e:

        if e is not None:
            print(traceback.format_exc())

        else:
            Console.error("Unexpected Error")


# enter_press_event = KeyboardEvent([ keyboard.Key.enter ], disable_live_tracking)

# enter_press_event.start()
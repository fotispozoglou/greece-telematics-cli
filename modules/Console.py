import os
from termcolor import colored

COLORS = {
    'grey',
    'red',
    'green',
    'yellow',
    'blue',
    'magenta',
    'cyan',
    'white'
}

class Console:

    @staticmethod
    def clear(  ):

        os.system("clear")

    @staticmethod
    def prompt( color, message, bg_color ):

        return input(f"{ colored( f' {message} ', color, on_color=bg_color, attrs=['bold'] ) } » ")

    @staticmethod
    def print( color, message, on_color = None, attrs = None ):

        print( colored( message, color, on_color, attrs ) )

    @staticmethod
    def info( message ):

        print(f'{ colored("[~]", "yellow") } { message }')

    @staticmethod
    def success( message ):

        print(f'{ colored("[+]", "green") } { message }')

    @staticmethod
    def error( message, flag = None ):

        print(f'{ colored("[-]", "red") }{ colored( f" ({ flag }) ", "blue" ) if flag != None else "" } { message }')
import os
from termcolor import colored

from prompt_toolkit import print_formatted_text, HTML

class Console:

    @staticmethod
    def clear(  ):

        os.system("clear")

    @staticmethod
    def print( color, message ):

        print_formatted_text(f"{ message }")

    @staticmethod
    def info( message ):

        html = f'<p><span fg="#F0A001"><b>[~]</b></span> { message }</p>'

        print_formatted_text(HTML(html))

    @staticmethod
    def success( message ):

        html = f'<p><span fg="#00F511"><b>[+]</b></span> { message }</p>'

        print_formatted_text(HTML(html))

    @staticmethod
    def error( message, flag = None ):

        html = f'<p><span fg="#F50801"><b>[-]</b></span> { message }</p>'

        print_formatted_text(HTML(html))
from termcolor import colored

class Menu:

    @staticmethod
    def print_option( index, option_name ):

        print(f"{ colored( f'[{ index }]', 'blue' ) } { option_name }")

    @staticmethod
    def input( prompt = 'insert' ):

        option = str(input(f"{ colored(prompt, 'blue') } > "))

        return option

    @staticmethod
    def select_option_prompt( prompt = 'select' ):

        option = input(f"{ colored(prompt, 'blue') } > ")

        return option

    @staticmethod
    def menu( options ):

        for index, option in enumerate( options ):

            Menu.print_option( index + 1, option[ 0 ] )

        option = Menu.select_option_prompt('select')

        if int(option) > len( options ):

            return Menu.menu( options )

        return options[ int(option) - 1 ][1]()
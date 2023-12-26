from modules.Option import Option
from inspect import signature

class Command:

    def __init__( self, base_command, action : callable, options : list[Option] = [] ):

        self.base_command = base_command
        self.options = options
        self.total_options = len( options )
        self.options_string = self.get_options_string( options )
        self.action = action
        self.action_params = signature( self.action ).parameters
        
    def get_options_string( self, options : list[Option] ):

        options_names = []

        for option in options:

            options_names.append( option.name )

        return ", ".join( options_names )
    
    def matches( self, user_command : str ):

        return user_command.startswith( self.base_command )

    def execute( self, user_command : str ):

        if len( self.action_params ) == 0:

            self.action()

            return

        args = " ".join(user_command.replace( self.base_command, '' ).split()).split(' ')

        try:

            self.action( *args )

        except TypeError as e:

            print(f"{ self.base_command } takes { self.total_options } options { self.options_string }")
from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout

from modules.Command import Command

class Menu():

    def __init__( self ):

        self.session = PromptSession()

        self.commands : list[Command] = []

    def register( self, command : Command ):

        self.commands.append( command )

    async def start_menu_routine( self ):

        while True:
            with patch_stdout():
                result = await self.session.prompt_async('> ')
            
            if result:
                
                for command in self.commands:

                    if result == "exit":

                        exit(0)

                    if command.matches( result ):

                        command.execute( result )
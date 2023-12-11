from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout

class Menu():

    def __init__( self ):

        self.session = PromptSession()

        self.commands = []

    def register( self, command, action ):

        self.commands.append({
            "command": command,
            "action": action
        })

    async def start_menu_routine( self ):

        while True:
            with patch_stdout():
                result = await self.session.prompt_async('> ')
            
            if result:
                
                for command in self.commands:

                    if result == "exit":

                        exit(0)

                    if result == command['command']:

                        command['action']()
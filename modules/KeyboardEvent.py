from pynput import keyboard

class KeyboardEvent:

    def __init__( self, keys, onKeyPress ):

        self.listener = keyboard.Listener(on_press=self.handleKeyPress)
        self.keys = keys
        self.onKeyPress = onKeyPress
        
    def start( self ):

        self.listener.start()

    def close( self ):

        self.listener.join()

    def handleKeyPress( self, keyPressed ):

        if keyPressed in self.keys:

            self.onKeyPress()

            # self.close()
OPTIONS_TYPE = {
    "string": "str",
    "int": "int"
}

class Option:

    def __init__( self, name, option_type ):

        self.name = name
        self.option_type = option_type
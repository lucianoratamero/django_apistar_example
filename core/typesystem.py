
from apistar import typesystem


class Object(typesystem.Object):
    '''
    Overrides API Star's Object type for one that removes
    all keys that have None values.
    '''

    def __init__(self, *args):
        obj = {key: value for key, value in args[0].items() if value is not None}
        super().__init__(**obj)

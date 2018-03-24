from apistar import typesystem

from core import typesystem as core_typesystem


class ProductName(typesystem.String):
    max_length = 100


class Product(core_typesystem.Object):
    properties = {
        'id': typesystem.Integer,
        'name': ProductName,
        'rating': typesystem.integer(default=None, minimum=1, maximum=5),
        'in_stock': typesystem.Boolean,
        'size': typesystem.enum(default=None, enum=['small', 'medium', 'large']),
    }

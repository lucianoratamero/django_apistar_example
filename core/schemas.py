from apistar import typesystem

from core import typesystem as core_typesystem


class ProductName(typesystem.String):
    max_length = 100


class ProductUpdate(core_typesystem.Object):
    properties = {
        'name': ProductName,
        'in_stock': typesystem.Boolean,
        'rating': typesystem.integer(default=None, minimum=1, maximum=5),
        'size': typesystem.enum(default=None, enum=['small', 'medium', 'large']),
    }


class Product(core_typesystem.Object):
    required = ['name', 'in_stock']

    properties = {
        'name': ProductName,
        'in_stock': typesystem.Boolean,
        'id': typesystem.integer(default=None),
        'rating': typesystem.integer(default=None, minimum=1, maximum=5),
        'size': typesystem.enum(default=None, enum=['small', 'medium', 'large']),
    }

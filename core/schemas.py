from apistar import types, validators


class ProductName(validators.String):
    max_length = 100


class Product(types.Type):
    id = validators.Integer(allow_null=True)
    name = ProductName()
    rating = validators.Integer(minimum=1, maximum=5, allow_null=True)
    in_stock = validators.Boolean()
    size = validators.String(enum=['small', 'medium', 'large'], allow_null=True)
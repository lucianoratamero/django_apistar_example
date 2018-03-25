
import typing

from core import schemas
from core import models


def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}


def list_products(name: schemas.ProductName) -> typing.List[schemas.Product]:
    queryset = models.Product.objects.all()

    if name:
        queryset = queryset.filter(name__icontains=name)

    return [schemas.Product(db_product.__dict__) for db_product in queryset]


def create_product(product: schemas.Product):
    if not product:
        return http.Response(status=400)

    db_product = models.Product(**product)
    db_product.save()

    return http.Response(schemas.Product(db_product.__dict__), status=201)


import typing

from apistar import http

from core import schemas
from core import models


def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}


def list_products(name=None) -> typing.List[schemas.Product]:
    queryset = models.Product.objects.all()

    if name:
        queryset = queryset.filter(name__icontains=name)

    return [schemas.Product(db_product.__dict__) for db_product in queryset]


def create_product(product: schemas.Product):
    db_product = models.Product(**product)
    db_product.save()

    return http.JSONResponse(schemas.Product(db_product.__dict__), status_code=201)


def update_product(product_id: int, product: schemas.Product):
    product.id = product_id
    db_products = models.Product.objects.filter(id=product_id)

    try:
        db_product = db_products.get()
    except models.Product.DoesNotExist:
        return http.Response('Not Found', status_code=404)

    db_product_data = db_product.__dict__
    db_product_data.update(product)

    validated_data = schemas.Product(db_product_data)
    db_products.update(**validated_data)

    return validated_data


def delete_product(product_id):
    try:
        db_product = models.Product.objects.get(id=product_id)
    except models.Product.DoesNotExist:
        return http.JSONResponse({}, status_code=404)

    db_product.delete()
    return http.JSONResponse({'id': product_id}, status_code=200)

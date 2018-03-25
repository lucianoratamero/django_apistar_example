
from apistar import Route

from core import views


routes = [
    Route('/', 'GET', views.welcome),
    Route('/products/', 'GET', views.list_products),
    Route('/products/', 'POST', views.create_product),
    Route('/product/{product_id}/', 'PUT', views.update_product),
    Route('/product/{product_id}/', 'DELETE', views.delete_product),
]

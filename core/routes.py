
from apistar import Route

from core import views


routes = [
    Route('/', 'GET', views.welcome),
    Route('/products/', 'GET', views.list_products),
    Route('/products/', 'POST', views.create_product),
]

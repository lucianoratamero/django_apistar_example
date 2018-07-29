
from apistar import Route
from apistar.server import Include
from django_apistar.authentication import routes as auth_routes

from core import views


routes = [
    Route('/', 'GET', views.welcome),
    Route('/products/', 'GET', views.list_products),
    Route('/products/', 'POST', views.create_product),
    Route('/product/{product_id}/', 'PUT', views.update_product),
    Route('/product/{product_id}/', 'DELETE', views.delete_product),
    Include('/auth', 'auth', auth_routes),
]

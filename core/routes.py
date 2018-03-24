
from apistar import Route

from core import views


routes = [
    Route('/', 'GET', views.welcome),
]

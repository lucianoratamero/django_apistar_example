
from model_mommy import mommy
from django_apistar.test import TestCase

from core import models
from core import schemas


class TestWelcome(TestCase):

    def setUp(self):
        self.url = self.reverse_url('welcome')

    def test_returns_without_name_querystring(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
        self.assertEqual({'message': 'Welcome to API Star!'}, response.json())

    def test_returns_with_name_querystring(self):
        url = self.url + '?name=lulu'
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual({'message': 'Welcome to API Star, lulu!'}, response.json())


class TestListProducts(TestCase):

    def setUp(self):
        self.url = self.reverse_url('list_products')

    def test_returns_product_list(self):
        products = mommy.make(models.Product, _quantity=3)

        response = self.client.get(self.url)
        content = response.json()

        self.assertEqual(200, response.status_code)
        for product in products:
            self.assertIn(schemas.Product(product.__dict__), content)

    def test_returns_list_with_name_querystring(self):
        url = self.url + '?name=Chocolate'
        mommy.make(models.Product, _quantity=3)
        named_product = mommy.make(models.Product, name='Chocolate')

        response = self.client.get(url)
        content = response.json()

        self.assertEqual(200, response.status_code)
        self.assertEqual([schemas.Product(named_product.__dict__)], content)

    def test_returns_list_of_products_with_containing_name(self):
        url = self.url + '?name=Chocolate'
        mommy.make(models.Product, _quantity=3)
        generic_chocolate = mommy.make(models.Product, name='Chocolate')
        garoto_chocolate = mommy.make(models.Product, name='chocolate garoto')

        response = self.client.get(url)
        content = response.json()

        self.assertEqual(200, response.status_code)
        self.assertEqual(2, len(content))
        self.assertIn(schemas.Product(generic_chocolate.__dict__), content)
        self.assertIn(schemas.Product(garoto_chocolate.__dict__), content)


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


class TestCreateProduct(TestCase):

    def setUp(self):
        self.url = self.reverse_url('list_products')

    def test_returns_400_for_empty_post(self):
        response = self.client.post(self.url, {})
        self.assertEqual(400, response.status_code)

    def test_required_fields(self):
        response = self.client.post(self.url, {'name': 'Chocolate'})
        self.assertEqual(400, response.status_code)
        self.assertEqual(b'{"in_stock":"The \\"in_stock\\" field is required."}', response.content)

        response = self.client.post(self.url, {'in_stock': False})
        self.assertEqual(400, response.status_code)
        self.assertEqual(b'{"name":"The \\"name\\" field is required."}', response.content)

    def test_creates_product(self):
        self.assertEqual(0, models.Product.objects.count())
        data = {'name': 'Chocolate', 'in_stock': False}
        expected_data = {
            'name': 'Chocolate',
            'in_stock': False,
            'id': 1,
            'rating': None,
            'size': None
        }

        response = self.client.post(self.url, data)

        self.assertEqual(201, response.status_code)
        self.assertEqual(1, models.Product.objects.count())
        self.assertEqual(expected_data, response.json())


class TestUpdateProduct(TestCase):

    def setUp(self):
        self.product = mommy.make(
            models.Product,
            name='Candy',
            in_stock=True,
            rating=3,
            size='small'
        )
        self.url = self.reverse_url('update_product', product_id=1)
        self.data = {
            'name': 'Chocolate',
            'in_stock': False,
            'rating': 5,
            'size': 'large',
        }

    def test_response_404_for_unexistent_product(self):
        url = self.reverse_url('update_product', product_id=9999)
        response = self.client.put(url, self.data)
        self.assertEqual(404, response.status_code)

    def test_updates_product(self):
        response = self.client.put(self.url, self.data)

        self.data.update({'id': 1})
        self.assertEqual(200, response.status_code)
        self.assertEqual(self.data, response.json())

    def test_valitation(self):
        self.data.update({'size': 'waay too big'})
        response = self.client.put(self.url, self.data)
        self.assertEqual(400, response.status_code)


class TestDeleteProduct(TestCase):
    def setUp(self):
        mommy.make(models.Product)

    def test_404_for_unexisting_product(self):
        url = self.reverse_url('delete_product', product_id=9999)
        response = self.client.delete(url)
        self.assertEqual(404, response.status_code)

    def test_200_and_delete_for_existing_product(self):
        url = self.reverse_url('delete_product', product_id=1)
        self.assertEqual(1, models.Product.objects.count())

        response = self.client.delete(url)

        self.assertEqual(200, response.status_code)
        self.assertEqual(0, models.Product.objects.count())

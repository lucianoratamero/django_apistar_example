
from django_apistar.test import TestCase


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

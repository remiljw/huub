from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Brand

# Create your tests here.
class OrdersTestCase(APITestCase):
    fixtures = ['initial_data.json']
    @classmethod
    def setUpTestData(cls) -> None:
        return super().setUpTestData()
    
    def test_orders_endpoint(self):
        response = self.client.get('/api/orders', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 4)

    def test_brands(self):
        response = self.client.get('/api/orders?brand=Apple', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 1)

    def test_deliveries_endpoint(self):
        response = self.client.get('/api/deliveries', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 3)

    def test_deliveries_order_reference(self):
        response = self.client.get('/api/deliveries?order_ref=3243ssg434', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 1)
    
    def tearDown(self) -> None:
        return super().tearDown()
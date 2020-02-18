"""

Test module
"""
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory
from core.models import *
from core.views import OrderViewSet


class OrderTest(TestCase):
    """

    """

    def setUp(self) -> None:
        """

        """
        self.customer = Customer.objects.create(name='Ali', phone_number='01171718495', address='Alex')
        PizzaType.objects.create(type='Margreitta')
        PizzaSize.objects.create(size='small')
        self.delivered_order = Order.objects.create(customer=self.customer, status=True)

    def test_create_order(self):
        """

        """
        data = {
            "customer_id": 1,
            "details": [
                {
                    "type": 1,
                    "size": 1
                }
            ]
        }
        request = APIRequestFactory().post("/orders/", data, format='json')
        brokerage_post = OrderViewSet.as_view({'post': 'create'})
        response = brokerage_post(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_order(self):
        """

        """
        data = {
            "details": [
                {
                    "type": 1,
                    "size": 1
                }
            ]
        }

        request = APIRequestFactory().patch("/orders/{}/".format(self.delivered_order.id), data, format='json')
        brokerage_patch = OrderViewSet.as_view({'patch': 'partial_update'})
        response = brokerage_patch(request,  pk=self.delivered_order.pk)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
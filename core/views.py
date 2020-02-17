"""
views module
"""
from rest_framework import viewsets
from core.models import PizzaSize, PizzaType, Pizza, Customer, Order
from core.serializer import PizzaTypeSerializer, PizzaSizeSerializer, PizzaSerializer, CustomerSerializer, \
    OrderSerializer


class PizzaSizeViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = PizzaSize.objects.all()
    serializer_class = PizzaSizeSerializer


class PizzaTypeViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = PizzaType.objects.all()
    serializer_class = PizzaTypeSerializer


class PizzaViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

"""
models serializers
"""
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from core.models import *


class PizzaSizeSerializer(serializers.ModelSerializer):
    """

    """

    class Meta:
        model = PizzaSize
        fields = ['size']


class PizzaTypeSerializer(serializers.ModelSerializer):
    """

    """

    class Meta:
        model = PizzaType
        fields = ('type', 'desc')


class PizzaSerializer(serializers.ModelSerializer):
    """

    """

    class Meta:
        model = Pizza
        fields = ('type', 'size', 'price')


class CustomerSerializer(serializers.ModelSerializer):
    """

    """
    class Meta:
        model = Customer
        fields = ('name', 'phone_number', 'address')


class OrderSerializer(serializers.ModelSerializer):
    """

    """
    customer = CustomerSerializer()
    details = PizzaSerializer(many=True)

    class Meta:
        model = Order
        fields = ('customer', 'details', 'status', 'total_price', 'created_at', 'updated_at')

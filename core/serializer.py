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


class GetPizzaSerializer(serializers.ModelSerializer):
    """

    """

    class Meta:
        model = Pizza
        fields = ('type', 'size', 'price')


class PizzaSerializer(serializers.ModelSerializer):
    """

    """

    class Meta:
        model = Pizza
        fields = ('id', 'type', 'size', 'price')


class CustomerSerializer(serializers.ModelSerializer):
    """

    """
    class Meta:
        model = Customer
        fields = ('name', 'phone_number', 'address')


class GetCustomerSerializer(serializers.ModelSerializer):
    """

    """
    class Meta:
        model = Customer
        fields = ['id']


class GetOrderSerializer(serializers.ModelSerializer):
    """

    """
    customer = CustomerSerializer()
    details = GetPizzaSerializer(many=True)

    class Meta:
        model = Order
        fields = ('customer', 'details', 'status', 'total_price', 'created_at', 'updated_at')


class OrderSerializer(serializers.ModelSerializer):
    """

    """
    customer = serializers.IntegerField()
    details = GetPizzaSerializer(many=True)

    class Meta:
        model = Order
        fields = ('customer', 'details')

    def create(self, validated_data):
        """

        :param validated_data:
        :return:
        """
        customer_id = validated_data.pop('customer')
        details_data = validated_data.pop('details')
        customer = Customer.objects.get(pk=customer_id)
        print(customer.name)
        new_order = Order.objects.create(customer=customer)
        print(new_order.status)
        for pizza in details_data:
            pizzaSerializer = GetPizzaSerializer(data=pizza)
            if pizzaSerializer.is_valid():
                # pizzaSerializer.save()
                Pizza.objects.create(order=new_order, type=pizza['type'], size=pizza['size'])
        return new_order

    def update(self, instance, validated_data):
        """

        :param instance:
        :param validated_data:
        :return:
        """
        if not instance.status:
            for pizza in validated_data.get('details'):
                pizzaSerializer = PizzaSerializer(data=pizza)
                if pizzaSerializer.is_valid():
                    pizzaSerializer.save()

            instance.save()
            return instance


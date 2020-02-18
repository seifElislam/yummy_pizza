"""
models serializers
"""
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from core.models import *


def get_valid_ids(objects_list):
    """

    """
    return [obj.id for obj in objects_list]


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
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Pizza
        fields = ('id','type', 'size', 'price')


class PizzaSerializer(serializers.ModelSerializer):
    """

    """
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Pizza
        fields = ('id', 'type', 'size', 'price', 'order')

    def update(self, instance, validated_data):
        """

        :param instance:
        :param validated_data:
        :return:
        """
        if not instance.order.status:
            instance.size = validated_data['size']
            instance.type = validated_data['type']
            instance.save()
            return instance
        raise serializers.ValidationError("This order has already been delivered")


class CustomerSerializer(serializers.ModelSerializer):
    """

    """
    name = serializers.CharField(max_length=250, read_only=True)
    phone_number = serializers.CharField(max_length=50, read_only=True)
    address = serializers.CharField(max_length=250, read_only=True)

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
        fields = ('id', 'customer', 'details', 'status', 'total_price', 'created_at', 'updated_at')


class OrderSerializer(serializers.ModelSerializer):
    """

    """
    customer_id = serializers.IntegerField(write_only=True)
    details = GetPizzaSerializer(many=True)
    id = serializers.IntegerField(read_only=True)
    status = serializers.BooleanField(required=False, default=False)

    class Meta:
        model = Order
        fields = ('id', 'status', 'customer_id', 'details')

    def create(self, validated_data):
        """

        :param validated_data:
        :return:
        """
        customer_id = validated_data.pop('customer_id')
        details_data = validated_data.pop('details')
        customer = Customer.objects.get(pk=customer_id)
        new_order = Order.objects.create(customer=customer)
        for pizza in details_data:
            Pizza.objects.create(order=new_order, type=pizza['type'], size=pizza['size'])
        return new_order

    def update(self, instance, validated_data):
        """

        :param instance:
        :param validated_data:
        :return:
        """
        if not instance.status:
            print(validated_data)
            instance.details.all().delete()
            for pizza in validated_data.get('details'):
                Pizza.objects.create(order=instance, type=pizza['type'], size=pizza['size'])
            if validated_data.get('status'):
                instance.status = validated_data.get('status')
            instance.save()
            return instance
        raise serializers.ValidationError("This order has already been delivered")


"""
models
"""
from django.db import models
from django.core.validators import RegexValidator


class PizzaSize(models.Model):
    """

    """
    size = models.CharField(max_length=50)


class PizzaType(models.Model):
    """

    """
    type = models.CharField(max_length=50)
    desc = models.CharField(max_length=250, null=True, blank=True)


class Customer(models.Model):
    """

    """
    name = models.CharField(max_length=250)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format:"
                                         " '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    address = models.CharField(max_length=250)


class Order(models.Model):
    """

    """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    total_price = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class Pizza(models.Model):
    """

    """
    type = models.OneToOneField(PizzaType, on_delete=models.CASCADE)
    size = models.OneToOneField(PizzaSize, on_delete=models.CASCADE)
    price = models.FloatField(default=0.0)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)


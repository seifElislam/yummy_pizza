"""
Admin Site models
"""

from django.contrib import admin
from core.models import Pizza, PizzaType, PizzaSize, Customer, Order

admin.site.register(PizzaSize)
admin.site.register(PizzaType)
admin.site.register(Pizza)
admin.site.register(Customer)
admin.site.register(Order)

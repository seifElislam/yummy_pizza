"""
Core App Urls
"""
from rest_framework import routers
from core.views import PizzaSizeViewSet, PizzaTypeViewSet, PizzaViewSet, CustomerViewSet, OrderViewSet

router = routers.SimpleRouter()
router.register(r'sizes', PizzaSizeViewSet)
router.register(r'types', PizzaTypeViewSet)
router.register(r'pizza', PizzaViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = []

urlpatterns += router.urls
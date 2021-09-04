from django.urls import include, path
from rest_framework import routers

from ecommerce.views import OrderItemsViewSet, OrderViewSet

router = routers.DefaultRouter()

router.register(r'orders', OrderViewSet)
router.register(r'orderitem', OrderItemsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

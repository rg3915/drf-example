from ecommerce.views import OrderItemsViewSet
from ecommerce.views import OrderViewSet
from rest_framework import routers
from django.urls import include, path

router = routers.DefaultRouter()

router.register(r'orders', OrderViewSet)
router.register(r'orderitem', OrderItemsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

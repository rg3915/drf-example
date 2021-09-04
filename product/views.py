from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from product.models import Product
from product.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)

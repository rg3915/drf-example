from ecommerce.models import OrderItems
from ecommerce.models import Order
from rest_framework import serializers


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderItemsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderItems
        fields = '__all__'

from ecommerce.models import OrderItems
from ecommerce.models import Order
from django.contrib import admin


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    exclude = ()


@admin.register(OrderItems)
class OrderItemsAdmin(admin.ModelAdmin):
    exclude = ()

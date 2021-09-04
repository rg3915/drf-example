from django.contrib import admin

from ecommerce.models import Order, OrderItems


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    exclude = ()


@admin.register(OrderItems)
class OrderItemsAdmin(admin.ModelAdmin):
    exclude = ()

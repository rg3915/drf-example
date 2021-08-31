from django.db import models

class Order(models.Model):    
    nf = models.CharField(max_length=255, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Orders"
    

class OrderItems(models.Model):    
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(null=True, default=0)
    price = models.DecimalField(null=True, default=0.0, max_digits=5, decimal_places=2)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Orderitem"
    


from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(
        null=True, default=0.0, max_digits=5, decimal_places=2)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Products"

from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=30, unique=True)
    sinopse = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Movies"


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

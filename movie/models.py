from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=30)
    sinopse = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Movies"

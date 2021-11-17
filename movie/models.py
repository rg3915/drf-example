from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=30, unique=True)
    sinopse = models.CharField(max_length=255, null=True, blank=True)
    rating = models.PositiveIntegerField(default=0)
    like = models.BooleanField(default=False)
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        verbose_name='categoria',
        related_name='movies',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name_plural = "Movies"

    def __str__(self):
        return f'{self.title}'


class Category(models.Model):
    title = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f'{self.title}'

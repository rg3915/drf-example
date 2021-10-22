from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.name


class Post(models.Model):
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.body

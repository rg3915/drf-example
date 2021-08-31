from django.db import models

class Author(models.Model):    
    name = models.CharField(max_length=255, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Authors"
    

class Post(models.Model):    
    body = models.TextField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Posts"
    


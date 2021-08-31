from blog.models import Post
from blog.models import Author
from django.contrib import admin


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    exclude = ()


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    exclude = ()

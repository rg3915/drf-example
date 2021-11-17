from django.contrib import admin

from movie.models import Category, Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'rating', 'like', 'category')
    search_fields = ('title', 'sinopse')
    list_filter = ('like', 'category')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ()

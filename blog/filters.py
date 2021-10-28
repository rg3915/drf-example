from django_filters import rest_framework as filters

from blog.models import Post


class PostFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    body = filters.CharFilter(field_name='body', lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ('title', 'body')

from rest_framework.pagination import PageNumberPagination


class CustomBlogResultsSetPagination(PageNumberPagination):
    page_size = 7
    page_size_query_param = 'page_size'
    max_page_size = 70

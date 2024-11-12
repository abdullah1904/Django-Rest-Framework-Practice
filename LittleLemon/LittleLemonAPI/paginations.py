from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomMenuItemPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'perpage'
    page_query_param = 'page'
    max_page_size = 20
    def get_paginated_response(self, data):
        return Response(data)

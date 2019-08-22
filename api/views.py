from collections import OrderedDict

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from api.serilizers import ArticleSerializer
from article.models import ArticleModel


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    max_page_size = 15

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('page_count', self.page.paginator.num_pages),
            ('articles', data)
        ]))


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = ArticleModel.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = super(ArticleViewSet, self).get_queryset()
        search_name = self.request.query_params.get('search', None)
        if search_name is not None:
            queryset = queryset.filter(title__contains=search_name)
        return queryset

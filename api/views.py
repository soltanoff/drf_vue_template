from collections import OrderedDict

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from api.serilizers import ArticleSerializer
from article.models import ArticleModel


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1
    max_page_size = 15

    def get_url(self, page_number):
        query_params = list(filter(lambda item: item[0] != self.page_query_param, self.request.query_params.items()))
        query_params.append((self.page_query_param, page_number))
        return '&'.join(map(lambda x: '%s=%s' % x, query_params))

    def get_next_link(self):
        if not self.page.has_next():
            return None
        url = self.request.get_full_path()
        page_number = self.page.next_page_number()
        return '%s?%s' % (url, self.get_url(page_number))

    def get_previous_link(self):
        if not self.page.has_previous():
            return None
        url = self.request.get_full_path()
        page_number = self.page.previous_page_number()
        return '%s?%s' % (url, self.get_url(page_number))
    
    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('page_count', self.page.paginator.count),
            ('current_page', self.page.number),
            ('next_page_url', self.get_next_link()),
            ('previous_page_url', self.get_previous_link()),
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

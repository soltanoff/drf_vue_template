from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination, _get_page_links, _get_displayed_page_numbers
from rest_framework.response import Response
from rest_framework.utils.urls import replace_query_param, remove_query_param

from api.serilizers import ArticleSerializer
from article.models import ArticleModel


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    max_page_size = 25
    
    def page_number_to_url(self, page_number):
        base_url = self.request.build_absolute_uri()
        if page_number == 1:
            return remove_query_param(base_url, self.page_query_param)
        else:
            return replace_query_param(base_url, self.page_query_param, page_number)

    def get_page_info(self):
        current = self.page.number
        page_numbers = _get_displayed_page_numbers(current, self.page.paginator.num_pages)
        page_links = _get_page_links(page_numbers, current, self.page_number_to_url)

        return [{'number': number, 'link': link.url } for number, link in zip(page_numbers, page_links)]

    def get_paginated_response(self, data):
        return Response({
            'pages_info': self.get_page_info(),
            'articles': data,
        })


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = ArticleModel.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = super(ArticleViewSet, self).get_queryset()
        search_name = self.request.query_params.get('search', None)
        if search_name is not None:
            return queryset.filter(title__contains=search_name)
        return queryset

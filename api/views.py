from rest_framework import viewsets

from api.serilizers import ArticleSerializer
from article.models import ArticleModel


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = ArticleModel.objects.all()
    serializer_class = ArticleSerializer

    def get_queryset(self):
        queryset = super(ArticleViewSet, self).get_queryset()
        search_name = self.request.query_params.get('search', None)
        if search_name is not None:
            queryset = queryset.filter(title__contains=search_name)
        return queryset

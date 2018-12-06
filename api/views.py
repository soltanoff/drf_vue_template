from rest_framework import viewsets

from api.serilizers import ArticleSerializer
from article.models import ArticleModel


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = ArticleModel.objects.all()
    serializer_class = ArticleSerializer

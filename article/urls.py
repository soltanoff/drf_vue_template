from django.urls import path

from article.apps import ArticleConfig
from article.views import ArticleView

app_name = ArticleConfig.name
urlpatterns = [
    path('', ArticleView.as_view(), name='index'),
]

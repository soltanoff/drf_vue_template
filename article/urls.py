from django.conf.urls import url

from article.apps import ArticleConfig
from article.views import ArticleView

app_name = ArticleConfig.name
urlpatterns = [
    url(r'', ArticleView.as_view(), name='index'),
]

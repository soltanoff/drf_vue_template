from rest_framework import routers

from api.views import ArticleViewSet

router = routers.DefaultRouter()

router.register(r'article/', ArticleViewSet)

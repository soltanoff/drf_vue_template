from rest_framework import routers
from rest_framework.documentation import get_schemajs_view
from rest_framework.schemas import get_schema_view

from api.views import ArticleViewSet

schema = get_schema_view(title='DRF & Vue.js API schema')
schema_js = get_schemajs_view(title='DRF & Vue.js API schema')
router = routers.DefaultRouter()
router.register('article', ArticleViewSet)

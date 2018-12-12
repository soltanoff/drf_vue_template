"""drf_vue_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from api.routers import router as api_router
from api.routers import schema as api_schema
from api.routers import schema_js as api_schema_js

urlpatterns = [
    url(r'^manage/', admin.site.urls),
    url('^schema$', api_schema),
    url('^schema_js$', api_schema_js),
    url(r'^api/', include(api_router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'', include('article.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

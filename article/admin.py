from django.contrib import admin

from article.models import ArticleModel


class ArticleAdminModel(admin.ModelAdmin):
    search_fields = ('title',)
    fieldsets = [
        (None, {'fields': ['title', 'content']}),
    ]


admin.site.register(ArticleModel, ArticleAdminModel)

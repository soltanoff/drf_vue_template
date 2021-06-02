from django.contrib import admin

from api.models import ArticleModel


@admin.register(ArticleModel)
class ArticleAdminModel(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('id', 'title')
    fieldsets = (
        ('Article', {'fields': ['title', 'content']}),
    )

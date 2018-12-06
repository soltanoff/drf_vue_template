from django.contrib import admin

from article.models import ArticleModel


@admin.register(ArticleModel)
class ArticleAdminModel(admin.ModelAdmin):
    search_fields = ('Title',)
    list_display = ('id', 'Title')
    fieldsets = (
        ('Article', {'fields': ['Title', 'Content']}),
    )

from django.views.generic import TemplateView


class ArticleView(TemplateView):
    template_name = 'index.html'

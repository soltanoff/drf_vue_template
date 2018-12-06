from django.db import models


class ArticleModel(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(name='Title', max_length=250)
    content = models.TextField(name='Content')

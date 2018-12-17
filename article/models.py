from django.db import models


class ArticleModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(name='title', max_length=250)
    content = models.TextField(name='content')

    class Meta:
       ordering = ['id']

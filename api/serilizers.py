from rest_framework import serializers

from api.models import ArticleModel


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleModel
        fields = '__all__'

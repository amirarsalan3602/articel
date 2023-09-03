from rest_framework import serializers
from .models import ArticleModel


class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ArticleModel
        fields = '__all__'


from django.conf.urls import url, include
from .models import Tag, Article
from rest_framework import routers, serializers, viewsets


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    article_tag = serializers.StringRelatedField(many=True)
    class Meta:
        model = Article
#        exclude = ['article_tag', 'article_img']
        exclude = ['article_img']
#        fields = '__all__'
from .models import Tag, Article
from .serializer import TagSerializer, ArticleSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .permissions import ReadOnly, IsAuthenticated_CUSTOM
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication


class TagViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated | ReadOnly]
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated_CUSTOM | ReadOnly]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    #queryset = Article.objects.all()
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = Article.objects.prefetch_related('article_tag')
    serializer_class = ArticleSerializer
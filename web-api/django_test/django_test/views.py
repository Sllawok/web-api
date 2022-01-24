from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from articles.models import Article, Tag
import random
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# Create your views here.

def home_page(request):
    random_idx = random.randint(0, Article.objects.count() - 1)
    #art_random = Article.objects.all()[random_idx]
    random_idx=0
    art_random = get_object_or_404(Article,id = random_idx+1)
    #return HttpResponse('This is the home page')
    return render(request, 'articles/index.html', {'article': art_random})



class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
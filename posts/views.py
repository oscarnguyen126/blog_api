from django.shortcuts import redirect
from .models import Post, User
from .serializers import PostSerializer
from django.http import JsonResponse


def listpost(request):
    posts = [PostSerializer(post).parse() 
             for post in Post.objects.all()]
    return JsonResponse(data={'posts': posts})


def detailpost(request, id):
    posts = [PostSerializer(post).parse()
             for post in Post.objects.filter(id=id)]
    return JsonResponse({'posts': posts})


from rest_framework import viewsets 
from .models import Post
from .serializers import PostSerializer
from django.conf import settings
from django.shortcuts import render

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

def blog_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog_list.html', {'posts': posts, 'LANGUAGES': settings.LANGUAGES,})
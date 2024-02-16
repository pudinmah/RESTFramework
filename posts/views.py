from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from posts.serializers import PostSerializer
from .models import Post


"""
Class based views
-.get()
-.post()
-.put()

Viewset
-.create()
-.list()
-.
"""

class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
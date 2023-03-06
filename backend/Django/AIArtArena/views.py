from django.shortcuts import render
from rest_framework import generics, renderers
from AIArtArena.models import Post
from AIArtArena.serializers import PostSerializer
from rest_framework.views import APIView
from django.http import FileResponse


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

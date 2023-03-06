from django.shortcuts import render
from rest_framework import generics, renderers
from AIArtArena.models import Post
from AIArtArena.serializers import PostSerializer
from rest_framework.views import APIView
from django.http import HttpResponse


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class JPEGRenderer(renderers.BaseRenderer):
    media_type = 'image/jpeg'
    format = 'jpg'
    charset = None
    render_style = 'binary'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        return data

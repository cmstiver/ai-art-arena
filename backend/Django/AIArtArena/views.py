from django.shortcuts import render
from rest_framework import generics, renderers
from AIArtArena.models import Post
from AIArtArena.serializers import PostSerializer, UserSerializer, RegisterSerializer
from rest_framework.views import APIView
from django.http import FileResponse
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from AIArtArena.permissions import IsOwnerOrReadOnly


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'posts': reverse('post-list', request=request, format=format)
    })


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.filter(is_private=False)
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        token = self.request.auth.key
        serializer.save(owner=Token.objects.get(
            key=token).user)


class UserPostList(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        posts = Post.objects.filter(owner=request.user)
        serializer = PostSerializer(
            posts, many=True, context={'request': request})
        return Response(serializer.data)


class UserLikeList(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        posts = Post.objects.filter(liked_by=request.user)
        serializer = PostSerializer(
            posts, many=True, context={'request': request})
        return Response(serializer.data)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly]


@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([TokenAuthentication])
def like_post(request, pk):
    post = Post.objects.filter(id=pk).first()

    if not post:
        return Response({"error": "Post not found"}, status=404)

    if request.user in post.liked_by.all():
        post.liked_by.remove(request.user)
        post.save()
    else:
        post.liked_by.add(request.user)
        post.save()
    serializer = PostSerializer(post, context={'request': request})
    return Response(serializer.data)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterUser(generics.CreateAPIView):
    serializer_class = RegisterSerializer

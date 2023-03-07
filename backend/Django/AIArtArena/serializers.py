from rest_framework import serializers
from AIArtArena.models import Post
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework.fields import SerializerMethodField


class PostSerializer(serializers.ModelSerializer):
    total_likes = SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'owner', 'url', 'created', 'total_likes', 'title', 'prompt', 'is_private', 'image0', 'image1', 'image2',
                  'image3', 'image4', 'image5', 'image6', 'image7', 'image8']

    def get_total_likes(self, instance):
        return instance.liked_by.count()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(
        many=True, view_name='post-detail', read_only=True)
    post_like = serializers.HyperlinkedRelatedField(
        many=True, view_name='post-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'posts', 'post_like']


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2',)

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

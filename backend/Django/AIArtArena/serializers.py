from rest_framework import serializers
from AIArtArena.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'created', 'title', 'image0', 'image1', 'image2',
                  'image3', 'image4', 'image5', 'image6', 'image7', 'image8']

from rest_framework import serializers
from .models import Posts

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['id', 'caption', 'hashtags', 'likes', 'comments', 'date', 'media', 'creator']
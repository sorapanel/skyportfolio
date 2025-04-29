from rest_framework import serializers
from .models import Article,Image,Video

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["id", "title", "description", "add_at", "update_at"]

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["id", "image", "article"]

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ["id", "video", "article"]
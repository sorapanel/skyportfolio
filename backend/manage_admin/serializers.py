from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class UserSerializer(serializers.ModelSerializer):
    """パスワードは書き込み専用"""
    password = serializers.CharField(write_only=True)
    is_superuser = serializers.BooleanField(read_only=True)
    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "is_superuser"]

    def create(self, validated_data):
        """
        新しいユーザ作成、パスワードをハッシュ化
        メアドは必須ではない
        """
        user = User.objects.create_user(
            username = validated_data["username"],
            email=validated_data.get("email", ""),
            password=validated_data["password"]
        )
        return user

class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField(read_only=True)
    instagram = serializers.CharField(read_only=True)
    x = serializers.CharField(read_only=True)
    github = serializers.CharField(read_only=True)
    image = serializers.ImageField(read_only=True)
    class Meta:
        model = Profile
        fields = ["id", "title", "subtitle", "description", "instagram", "x", "github", "image", "bgimage"]
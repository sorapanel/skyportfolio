from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Profile
from .serializers import UserSerializer, ProfileSerializer

class UserViewSet(viewsets.ModelViewSet):
    """ユーザ登録用のAPI"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.filter(id=1)
    serializer_class = ProfileSerializer
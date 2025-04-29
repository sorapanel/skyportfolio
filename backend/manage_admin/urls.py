from rest_framework import routers
from .views import UserViewSet, ProfileViewSet
from django.urls import path,include

router = routers.DefaultRouter()
router.register(r'_user', UserViewSet)
router.register(r'_profile', ProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
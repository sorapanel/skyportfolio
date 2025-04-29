from rest_framework import routers
from .views import ArticleViewSet, ImageViewSet, VideoViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'_article', ArticleViewSet)
router.register(r'_image', ImageViewSet)
router.register(r'_video', VideoViewSet)

urlpatterns = [
    path('', include(router.urls))
]

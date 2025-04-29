from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=64, blank=False, null=False)
    description = models.TextField(blank=True, null=True, max_length=1000)
    add_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Image(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='article_images/')

class Video(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='videos')
    video = models.FileField(upload_to='article_videos/')


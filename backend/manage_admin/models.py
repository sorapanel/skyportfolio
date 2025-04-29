from django.db import models

# Create your models here.
class Profile(models.Model):
    title = models.CharField(blank=False, null=True, max_length=256)
    subtitle = models.CharField(blank=True, null=True, max_length=256)
    description = models.TextField(blank=True, null=True, max_length=1000)
    instagram = models.CharField(blank=False, null=True, max_length=256)
    x = models.CharField(blank=False, null=True, max_length=256)
    github = models.CharField(blank=False, null=True, max_length=256)
    image = models.ImageField(upload_to='profile_images/', null=True)
    bgimage = models.ImageField(upload_to='profile_bgimages/', null=True)
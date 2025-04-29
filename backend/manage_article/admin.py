from django.contrib import admin
from .models import Article,Image,Video

# Register your models here.
admin.site.register(Article)
admin.site.register(Image)
admin.site.register(Video)
from django.contrib import admin
from .models import Post, NewsAPIPost

# Register your models here.
admin.site.register(Post)
admin.site.register(NewsAPIPost)
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Post, NewsAPIPost

class StaticSitemap(Sitemap):
    changefreq = "monthly"
    priority = 1.0
    
    def items(self):
        urls = ['/', '/posts/tech', '/posts/sport', '/posts/polemic', '/posts/celebrity']
        
        return urls
        
    def location(self, item):
        return item
        

class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 8.0

    def items(self):
        
        articles = Post.objects.filter().order_by("-created_at")
        
        return list(articles)

    def location(self, item):
        
        if item and isinstance(item, Post):
            return reverse("post_view", args=[item.slug])

class NewsAPIPostSitemap(Sitemap):
    changefreq = "hourly"
    priority = 8.0
    
    def items(self):
        posts = NewsAPIPost.objects.filter().order_by("-created_at")
        
        return list(posts)
        
    def location(self, items):
        if items and isinstance(items, NewsAPIPost):
            return reverse("newsapi_post_view", args=[items.slug])
from django.shortcuts import render, redirect

from django.views.generic import View
from django.http import HttpResponse

from .utils import fetch_posts

from .models import Post, NewsAPIPost
from django.http import JsonResponse

from .tasks import task_get_posts_and_save

# Create your views here.
class HomeView(View):
    def get(self, request):
        
        post = Post.objects.all().order_by("-created_at")[:3]
        
        post_destaque = Post.get_destaque_post()
        
        post_category= Post.get_post_of_each_category()
            
        sugested_post = Post.get_sugested_post(post)
        
        posts_other_sources = NewsAPIPost.get_newsapi_posts()
        
        context = {
            "all_posts": post,
            
            "post_category": post_category,
            
            "sugested_post": sugested_post,
            
            "posts_other_sources": posts_other_sources,
            
            "destaque": post_destaque,
        }
        
        return render(request, "blog/posts.html", context)
        
        
class PostsView(View):
    def get(self, request, category):
        
        ##Query data
        posts = Post.objects.filter(category = category).order_by("-created_at")
        
        post_destaque = Post.get_destaque_post()
        
        post_category= Post.get_post_of_each_category()
            
        sugested_post = Post.get_sugested_post(posts)
        
        posts_other_sources = NewsAPIPost.get_newsapi_posts()
        
        context = {
            "all_posts": posts,
            
            "post_category": post_category,
            
            "sugested_post": sugested_post,
            
            "posts_other_sources": posts_other_sources,
            
            "destaque": post_destaque,
           }
        
        return render(request, "blog/posts.html", context)
        
        
        
class ShowAPostView(View):
    def get(self, request, title):
        
        post = Post.objects.get(title = title)
        
        post_category= Post.get_post_of_each_category()
        
        post_destaque = Post.get_destaque_post()
        
        posts_other_sources = NewsAPIPost.get_newsapi_posts()
        
        #sugested_post = Post.get_sugested_post(post)
        
        sugested_post = None
        context = {
            "post": post,
            "post_category": post_category,
            
            "destaque": post_destaque,
            
            "posts_other_sources": posts_other_sources,
            
            "sugested_post": sugested_post
        }
        return render(request, "blog/post.html", context)
        
class ShowANewsAPIPostView(View):
    def get(self, request, title):
        
        post = NewsAPIPost.objects.get(title = title)
        
        post_category= Post.get_post_of_each_category()
        
        post_destaque = Post.get_destaque_post()
        
        posts_other_sources = NewsAPIPost.get_newsapi_posts()
        
        #sugested_post = Post.get_sugested_post(post)
        
        sugested_post = None
        context = {
            "post": post,
            "post_category": post_category,
            
            "destaque": post_destaque,
            
            "posts_other_sources": posts_other_sources,
            
            "sugested_post": sugested_post
        }
        return render(request, "blog/newsapi_post.html", context)
        
        
class UpdatePostView(View):
    def get(self, request):
        task_get_posts_and_save()
        
        return HttpResponse("Posts actualizados com sucesso!")
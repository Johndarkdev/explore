from django.shortcuts import render, redirect, get_object_or_404

from django.views.generic import View
from django.http import HttpResponse

from .utils import fetch_posts

from .models import Post, NewsAPIPost
from django.http import JsonResponse

from .tasks import task_get_posts_and_save

# Create your views here.
class HomeView(View):
    def get(self, request):
        
        post_destaque = Post.get_destaque_post()
        
        posts = Post.objects.all().exclude(category="destaque").order_by("-created_at")
        
        post_category= Post.get_post_of_each_category()
            
        sugested_post = Post.get_sugested_post(posts, post_category)
        
        posts_other_sources = NewsAPIPost.get_newsapi_posts()[:10]
        
        """Evitar posts duplicados numa só página"""
        
        for p in post_category:
            if p != None:
                posts = posts.exclude(pk = p.pk)
        
        context = {
            "all_posts": posts,
            
            "post_category": post_category,
            
            "sugested_post": sugested_post,
            
            "posts_other_sources": posts_other_sources,
            
            "destaque": post_destaque,
        }
        
        return render(request, "blog/posts.html", context)
        
        
class PostsView(View):
    def get(self, request, category):
        
        ##Query data
        posts = Post.objects.filter(category = category).order_by("-created_at")[:8]
        
        post_destaque = Post.get_destaque_post()
        
        post_category= Post.get_post_of_each_category()
            
        sugested_post = Post.get_sugested_post(posts, post_category)
        
        posts_other_sources = NewsAPIPost.get_newsapi_posts()[:10]
        
        """Evitar posts duplicados numa só página"""
        
        for post in posts:
            if post in post_category:
                post_category.remove(post)
            
        context = {
            "all_posts": posts,
            
            "post_category": post_category,
            
            "sugested_post": sugested_post,
            
            "posts_other_sources": posts_other_sources,
            
            "destaque": post_destaque,
            
            "category": category
           }
        
        return render(request, "blog/posts.html", context)
        
        
        
class ShowAPostView(View):
    def get(self, request, slug):
        
        post = get_object_or_404(Post, slug = slug)
        
        post_category= Post.get_post_of_each_category()
        
        post_destaque = Post.get_destaque_post()
        
        posts_other_sources = NewsAPIPost.get_newsapi_posts()[:10]
        
        sugested_post = Post.get_sugested_post(post, post_category)
        
        """Excluir um post dentro de post_category se igual ao post"""
        if post in post_category:
            post_category.remove(post)
            
        
        
        context = {
            "post": post,
            "post_category": post_category,
            
            "destaque": post_destaque,
            
            "posts_other_sources": posts_other_sources,
            
            "sugested_post": sugested_post
        }
        return render(request, "blog/post.html", context)
        
class ShowANewsAPIPostView(View):
    def get(self, request, slug):
        
        post = get_object_or_404(NewsAPIPost, slug = slug)
        
        post_category= Post.get_post_of_each_category()
        
        post_destaque = Post.get_destaque_post()
        
        posts_other_sources = NewsAPIPost.get_newsapi_posts().exclude(pk=post.pk)
        
        sugested_post = Post.get_sugested_post(post, post_category)
        
        context = {
            "post": post,
            "post_category": post_category,
            
            "destaque": post_destaque,
            
            "posts_other_sources": posts_other_sources,
            
            "sugested_post": sugested_post
        }
        return render(request, "blog/newsapi_post.html", context)

from django.http import JsonResponse
import cloudinary.uploader       
        
class UpdatePostView(View):
    def get(self, request):
        task_get_posts_and_save()
        
        return HttpResponse("Posts actualizados com sucesso!")
        #result = cloudinary.uploader.upload("/storage/emulated/0/Project/Django/explore/media/uploads/2024/11/17/pexels-ahmet-yigit-koksal-2083491421-29293150.jpg")
        #return JsonResponse(result)
        

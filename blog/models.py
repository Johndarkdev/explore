from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import get_object_or_404

#ckeditor importations
from django_ckeditor_5.fields import CKEditor5Field


class Post(models.Model):
    title = models.CharField(max_length= 255, null= False, blank= False)
    summary = CKEditor5Field('Sumário', config_name='default')
    content = CKEditor5Field('Conteúdo', config_name='default')
    
    author = models.ForeignKey(User, on_delete= models.PROTECT)
    
    category = models.CharField(max_length=100)
    
    url_to_image = models.CharField(max_length=255, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add= True)
    
    class Meta:
        ordering = ["-created_at"]
        
    def __str__(self):
        return self.title
        
    ##Methods of Post class
    def get_destaque_post():
        post_destaque = Post.objects.filter(category= "destaque").order_by("-created_at")[:3]
        
        post_dic = {
            'destaque1': None,
            'destaque2': None,
            'destaque3': None
        }
        
        i = 0
        for item in post_destaque:
            post_dic[f'destaque{i}']= item
            i += 1
            
        return post_dic
        
        
    #Get post of each  Category
    def get_post_of_each_category():
        celebrity_post = Post.objects.filter(category = "celebrity").order_by("-created_at").first()
        
        sport_post = Post.objects.filter(category = "sport").order_by("-created_at").first()
        
        tech_post = Post.objects.filter(category = "tech").order_by("-created_at").first()
        
        post_category = [
            celebrity_post, sport_post, tech_post
        ]
        
        return post_category
        
    
    ##Get sugested post    
    def get_sugested_post(post):
        
        sugested_posts = None
        
        sugested_posts = Post.objects.filter().order_by("-created_at")
        
    
        for p in post:
                sugested_posts = sugested_posts.exclude(pk = p.pk)
       
        return sugested_posts
        
        
    
#NewsAPIPost Post class
class NewsAPIPost(models.Model):
    name = models.CharField(max_length = 255)
    
    title = models.CharField(max_length = 255)
    
    summary = models.TextField()
    
    content = models.TextField()
    
    author = models.CharField(max_length = 255)
    
    urlToImage = models.CharField(max_length = 500)
    
    urlToPost = models.CharField(max_length = 500)
    
    category = models.CharField(max_length=100)
    
    created_at = models.DateTimeField()
    
    class Meta:
        ordering = ["-created_at"]
    
    def __str__(self):
        return self.title
    
    def get_newsapi_posts():
        posts = NewsAPIPost.objects.all().order_by("-created_at")[:5]
        
        return posts
        
   ##Save in db     
    def save_in_db(all_posts, category):
        
        for post in all_posts:
            
            p = NewsAPIPost()
            p.name = post["source"]["name"]
            
            p.title = post["title"]
            p.summary = post["description"]
            
            p.content = post["content"]
            
            p.author = post["author"]
            
            p.urlToImage = post["urlToImage"]
            
            p.urlToPost = post["url"]
            
            p.created_at = post["publishedAt"]
            
            p.category = category
        
            p.save()

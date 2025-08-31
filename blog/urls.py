from django.urls import path
from .views import HomeView, PostsView, ShowAPostView, ShowANewsAPIPostView, UpdatePostView

urlpatterns = [
    path('', HomeView.as_view(), name = "home_view"),
    
    path('posts/<str:category>', PostsView.as_view(), name= "posts_view"),
    
    
    path('post/<slug:slug>', ShowAPostView.as_view(), name="post_view"),
    
    path('newsapi/post/<slug:slug>', ShowANewsAPIPostView.as_view(), name="newsapi_post_view"),
    
    path('update_posts/', UpdatePostView.as_view(), name="update_posts"),
]
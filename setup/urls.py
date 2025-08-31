from django.contrib import admin
from django.urls import path, include

from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap

from blog.sitemaps import PostSitemap, StaticSitemap, NewsAPIPostSitemap

sitemaps = {
    'static_urls': StaticSitemap(),
    'posts_urls': PostSitemap(),
    
    'newsapi_posts_urls': NewsAPIPostSitemap
}


urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    
    path("admin/", admin.site.urls),
    
   path('ckeditor5', include('django_ckeditor_5.urls')),
    
    path('', include('blog.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
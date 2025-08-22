from .utils import fetch_posts

def task_get_posts_and_save():
    
##Get general news 
    fetch_posts("news+today+world", "ultima hora", "publishedAt")
    
  
##Get sport news
    fetch_posts("sport", "desporto", "publishedAt")
    
##Get Tech news
    fetch_posts("tech", "tecnologia", "publishedAt")
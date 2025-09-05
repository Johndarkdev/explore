from .utils import fetch_posts

def task_get_posts_and_save():
    
##Get general news 
    fetch_posts('news', 'news', "popularity")
    
  
##Get sport news
    fetch_posts('("La Liga" OR "Premier League" OR "Serie A" OR "Bundesliga" OR "Ligue 1" OR "Champions League" OR "Europa League") AND (match OR game OR fixture OR result) AND "Real Madrid" AND "Barcelona" ', "sport", "popularity")
    
##Get Tech news
    fetch_posts('technology', "tech", "popularity")
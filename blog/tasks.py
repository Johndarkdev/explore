from .utils import fetch_posts

def task_get_posts_and_save():
    
##Get general news 
    #fetch_posts("notícias OR actualidade OR assuntos do dia", "ultima hora", "publishedAt")
    
  
##Get sport news
    fetch_posts('("La Liga" OR "Premier League" OR "Serie A" OR "Bundesliga" OR "Ligue 1" OR "Champions League" OR "Europa League") AND (match OR game OR fixture OR result) AND "Real Madrid" AND "Barcelona" ', "sport", "publishedAt")
    
##Get Tech news
    fetch_posts('tech', "tech", "publishedAt")
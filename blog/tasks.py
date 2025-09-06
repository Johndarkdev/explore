from .utils import fetch_posts

def task_get_posts_and_save():
    
    # Notícias gerais
    fetch_posts(
    '(world OR international OR breaking) AND (politics OR economy OR society)', 
    'news', 
    'popularity'
)

    # Desporto
    fetch_posts(
    '("La Liga" OR "Premier League" OR "Serie A" OR "Bundesliga" OR "Ligue 1" OR "Champions League" OR "Europa League") AND (match OR result OR highlights OR goals OR score) AND ("Real Madrid" OR "Barcelona" OR "Manchester City" OR "Bayern Munich")', 
    'sport', 
    'popularity'
)

    # Tecnologia
    fetch_posts(
    '(AI OR "artificial intelligence" OR "machine learning" OR innovation OR startup OR "big tech" OR cybersecurity OR gadgets OR smartphones OR software OR cloud)', 
    'tech', 
    'popularity'
)
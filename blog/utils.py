import requests
from .models import NewsAPIPost
from django.conf import settings
from datetime import date

#Fetch General News
def fetch_posts(query, category, sortBy):
    
      
    params = {
         'q': query,
        
        'language': 'pt',
        
        'sortBy': sortBy,
        
        'pageSize': 3,
        
        #'from': date.today(),
        
        'apiKey': settings.NEWSAPI_KEY,
    }
    
    url = "https://newsapi.org/v2/everything"
    
    try:
        response = requests.get(url=url, params=params)
        
        response.raise_for_status()
        
    except:
        e = requests.exceptions.RequestException
        return {
            'erro': str(e),
        }
            
    if response.status_code == 200:
        
        
        data = response.json()
        #print(data)
        NewsAPIPost.save_in_db(data["articles"], category)
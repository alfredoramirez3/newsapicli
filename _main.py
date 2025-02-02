

from enum import Enum
import json

import requests
import rich


apiKey='cf96fa53ce3c40f2835d7a955e868de1'

# move to news/news/utils.py
def dict_to_json(_dict):
    return json.dumps(_dict)

# move to news/news/utils.py 
def get_articles(url: str):
    news = requests.get(url)
    data = json.loads(news.content)
    articles = data['articles']
    return articles

# move to news/news/utils.py 
def output_articles(articles):

    for article in articles:
        article = dict_to_json(article)
        rich.print_json(article) 
           
    return None 

# move to news/news/options.py
class CategoryOption(str, Enum):
    business = "business"
    entertainment = "entertainment"
    general = "general"
    health = "health"
    science = "science"
    sports = "sports" 
    technology = "technology" 
 

# move to news/news/cli/articles.py
def topheadlines(query: str = None, category: CategoryOption = None):
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={apiKey}'
    if category:
        category = category.value
        # url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={apiKey}&category={category}'
        url += f'&category={category}'
         
        
    if query:
        url = url + f'&q={query}'
        
    articles = get_articles(url)
    output_articles(articles)

    rich.print(f"num_articles={len(articles)}") 
    rich.print(f"url={url}")

    return None

# move to news/news/cli/articles.py
def everything(query, from_date: str =None, to_date:str =None):
    #'https://newsapi.org/v2/everything?apiKey={apiKey} + &q={q} [+ &from{from_date} + &to{to_date}]
    url = f'https://newsapi.org/v2/everything?apiKey={apiKey}'
 
    if query:
        url += f'&q={query}'
    else:
        url += f'&qTrump' # to be removed
        
    if from_date and to_date:
        url += f'&from={from_date}'
        url += f'&to={to_date}'
        
        
    articles = get_articles(url)
    output_articles(articles)

    rich.print(f"num_articles={len(articles)}") 
    rich.print(f"url={url}")

    return None

if __name__ == "__main__":
    # topheadlines()
    # topheadlines(category=Category.technology)    
    # topheadlines(query='Apple', category=CategoryOption.technology)
    # topheadlines(query='DeepSeek', category=CategoryOption.technology)
    # topheadlines(query='DeepSeek')
    # topheadlines(query='Trump')

    # everything(query="", from_date="", to_date="") pattern
    # everything(query="DeepSeek")
    # everything(query="DeepSeek", from_date='2025-01-01', to_date='2025-01-02')
    everything(query="Trump")



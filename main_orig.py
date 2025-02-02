# Code from:
# https://medium.com/write-a-catalyst/collection-of-10-amazing-python-automation-scripts-2f93695de8ab

from plyer import notification
import requests
import json
country_code = input("Enter the country code for the news: ")
api_key = input("Enter the api key: ")
news = requests.get(
    f'https://newsapi.org/v2/top-headlines?country={country_code}&apiKey={api_key}')
data = json.loads(news.content)
for article in data['articles']:
    notification.notify(
        title=article['title'][:20],
        message=article['description'][:44],
        timeout=5,
        toast=False)
from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='cf96fa53ce3c40f2835d7a955e868de1')

# /v2/top-headlines
def top_headlines():
    return newsapi.get_top_headlines(q='bitcoin',
                                    sources='bbc-news,the-verge',
                                    category='business',
                                    language='en',
                                    country='us')

# /v2/everything
def all_articles():
    return newsapi.get_everything(q='bitcoin',
                                  sources='bbc-news,the-verge',
                                  domains='bbc.co.uk,techcrunch.com',
                                  from_param='2017-12-01',
                                  to='2017-12-12',
                                  language='en',
                                  sort_by='relevancy',
                                  page=2)

# /v2/top-headlines/sources
def sources():
    return newsapi.get_sources()

if __name__ == "__main__":
    print(top_headlines())
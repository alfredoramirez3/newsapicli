import csv
from enum import Enum
import json
import os
import sys
from typing import List

from dotenv import load_dotenv
import requests
import rich
from rich.console import Console
from rich.table import Table
import typer


if os.path.isfile(".env"):
    load_dotenv()
 
    
# print(os.environ.get("NEWSAPI_KEY"))
apiKey = os.environ.get("NEWSAPI_KEY")

# move to news/news/options.py
class CategoryOption(str, Enum):
    business = "business"
    entertainment = "entertainment"
    general = "general"
    health = "health"
    science = "science"
    sports = "sports" 
    technology = "technology" 
 

# move to news/options.py    
class OutputOption(str, Enum):
    csv = "csv"
    json = "json"
    table = "table"

# move to news/utils.py
def dict_to_json(_dict):
    return json.dumps(_dict)


# move to news/utils.py
# Function to flatten JSON
def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


# move to news/utils.py 
def output_articles(articles: List[dict], output: OutputOption.table):
    if output == OutputOption.json:
        rich.print_json(json.dumps(articles))
    elif output == OutputOption.csv:
        list_of_dict = []
        for d in articles:
            list_of_dict.append(flatten_json(d))
            
        fieldnames = list_of_dict[0].keys()
        writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(list_of_dict)        
    elif output == OutputOption.table:
        table = Table()
        list_of_dict = []
        for d in articles:
            list_of_dict.append(flatten_json(d))        
        
        headers = list_of_dict[0].keys()
        table.add_column("")
        for h in headers:
            table.add_column(str(h))

        for article in list_of_dict:
            table.add_row(
                *[str(list_of_dict.index(article) + 1)] + [str(a) for a in article.values()]
            )

        console = Console()
        console.print(table)
           
    return None 

# move to news/newsapi.py 
def get_articles(url: str):
    news = requests.get(url)
    data = json.loads(news.content)
    articles = data['articles']
    return articles


everything_app = typer.Typer()
topheadlines_app = typer.Typer()

# move to news/cli/article.py
@everything_app.command(name="everything", help="newsapi everything endpoint")
def articles_from_everything(
    query:      str = typer.Option(..., "--query", "-q", help="subject, such as Apple | DeepSeek | Trump"),
    from_date:  str = typer.Option(None, "--from_date", "-f", help="starting date"),
    to_date:    str = typer.Option(None, "--to_date", "-t", help="ending date"),
    sort_by:    str = typer.Option(None, "--sort_by", "-s", help="sort by publishedAt"),
    output: OutputOption = typer.Option(OutputOption.table, "--output", "-o", help="output format"),):
    
    # build the request url
    url = f'https://newsapi.org/v2/everything?apiKey={apiKey}'
 
    if query:
        url += f'&q={query}'
    else:
        url += f'&qTrump' # to be removed
        
    if from_date and to_date:
        url += f'&from={from_date}'
        url += f'&to={to_date}'
        
    # get and output articles
    articles = get_articles(url)
    output_articles(articles, output=output)

    # output metadaa
    rich.print(f"num_articles={len(articles)}")
    rich.print(f"*query={query}, from_date={from_date}, to_date={to_date}, sort_by={sort_by}")
    rich.print(f"url={url}")

    return None


# move to news/cli/article.py
@topheadlines_app.command(name="topheadlines", help="newsapi top-headlines endpoint")
def articles_from_topheadlines(
    query:      str             = typer.Option(None, "--query", "-q", help="subject, such as Apple | DeepSeek | Trump"),
    category:   CategoryOption  = typer.Option(None, "--category", "-c", help="category option"),
    output: OutputOption = typer.Option(OutputOption.table, "--output", "-o", help="output format"),): 
    
    # build the request url
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={apiKey}'
    if category:
        category = category.value
        # url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={apiKey}&category={category}'
        url += f'&category={category}'
         
    if query:
        url = url + f'&q={query}'
    
    # get and output articles   
    articles = get_articles(url)
    output_articles(articles, output=output)

    # print metadata
    rich.print(f"num_articles={len(articles)}")
    rich.print(f"query={query}, category={category}")
    rich.print(f"url={url}")

    return None

app = typer.Typer()
app.add_typer(everything_app)
app.add_typer(topheadlines_app)

if __name__ == "__main__":
    app()
   
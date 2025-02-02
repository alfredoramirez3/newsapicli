import os

import rich
import typer
from dotenv import load_dotenv

from newsapicli.options import CategoryOption
from newsapicli.options import OutputOption
from newsapicli.newsapi import get_articles
from newsapicli.newsapi import output_articles


if os.path.isfile(".env"):
    load_dotenv()

apiKey = os.environ.get("NEWSAPI_KEY")


everything_app = typer.Typer()
topheadlines_app = typer.Typer()


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

    # output metadata; ok with json and table; problem with csv
    rich.print(f"num_articles={len(articles)}")
    rich.print(f"*query={query}, from_date={from_date}, to_date={to_date}, sort_by={sort_by}")
    rich.print(f"url={url}")

    return None


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

    # output metadata; ok with json and table; problem with csv
    rich.print(f"num_articles={len(articles)}")
    rich.print(f"query={query}, category={category}")
    rich.print(f"url={url}")

    return None
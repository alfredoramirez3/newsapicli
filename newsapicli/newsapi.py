import csv
import json
import sys
from typing import List

import requests
import rich
from rich.console import Console
from rich.table import Table

# from newsapicli.utils import flatten_json # deprecate
from newsapicli.options import OutputOption

from newsapicli.utils import flatten


def get_articles(url: str):
    news = requests.get(url)
    data = json.loads(news.content)
    articles = data['articles']
    return articles


def output_articles(articles: List[dict], output: OutputOption.table):
    if output == OutputOption.json:
        rich.print_json(json.dumps(articles))
    elif output == OutputOption.csv:
        list_of_dict = []
        for d in articles:
            # list_of_dict.append(flatten_json(d)) # rremove
            list_of_dict.append(flatten(d))
            
        fieldnames = list_of_dict[0].keys()
        writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(list_of_dict)        
    elif output == OutputOption.table:
        table = Table()
        list_of_dict = []
        for d in articles:
            # list_of_dict.append(flatten_json(d)) # remove
            list_of_dict.append(flatten(d))
        
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
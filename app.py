import os

from dotenv import load_dotenv
import typer

from newsapicli.cli.article import everything_app
from newsapicli.cli.article import topheadlines_app

"""
if os.path.isfile(".env"):
    load_dotenv()
# # print(os.environ.get("NEWSAPI_KEY"))
apiKey = os.environ.get("NEWSAPI_KEY")
print(apiKey) # debug code 
"""

app = typer.Typer()
app.add_typer(everything_app)
app.add_typer(topheadlines_app)


if __name__ == "__main__":
    app()
   
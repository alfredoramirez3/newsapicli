import json
import csv
import sys

import rich

# Sample JSON data
json_data =   [{
    "source": {
      "id": "usa-today",
      "name": "USA Today"
    },
    "author": "Jonathan Limehouse",
    "title": "19 people found dead on vessel near Caribbean nation of St. Kitts and Nevis - USA TODAY",
    "description": "Authorities in the Caribbean nation of St. Kitts and Nevis are investigating the deaths of 19 people who were found aboard a drifting vessel.",
    "url": "https://www.usatoday.com/story/news/world/2025/01/31/19-dead-people-st-kitts-and-nevis/78086457007/",
    "urlToImage": "https://www.usatoday.com/gcdn/authoring/authoring-images/2025/01/31/USAT/78087239007-1738253294-whats-app-image-20250130-at-115911.jpeg?crop=1198,673,x2,y285&width=1198&height=673&format=pjpg&auto=webp",
    "publishedAt": "2025-01-31T17:32:47Z",
    "content": "An investigation is underway in the Caribbean nation of St. Kitts and Nevis after 19 people were found dead aboard a vessel, authorities said.\r\nThe St. Kitts and Nevis Defence Force (SKNDF) received … [+1302 chars]"
  },
  {
    "source": {
      "id": "espn",
      "name": "ESPN"
    },
    "author": "Tim Bontemps, Brian Windhorst",
    "title": "NBA intel: Three teams are forming a Wemby blockade atop the West - ESPN",
    "description": "Victor Wembanyama is charging toward West supremacy. Problem is, OKC, Houston and Memphis aren't going anywhere. And each can get even stronger at the trade deadline.",
    "url": "https://www.espn.com/nba/insider/story/_/id/43627075/nba-trade-intel-how-three-west-leaders-prepping-deadline",
    "urlToImage": "https://a3.espncdn.com/combiner/i?img=%2Fphoto%2F2025%2F0130%2Fr1445466_1296x729_16%2D9.jpg",
    "publishedAt": "2025-01-31T17:14:00Z",
    "content": "Jan 31, 2025, 12:14 PM ET\r\nLast week, the NBA descended on Paris for a week of events and a pair of games that were essentially a Victor Wembanyama festival. He'd turned 21 just two weeks before, but… [+2421 chars]"
  },
  {
    "source": {
      "id": "null",
      "name": "BBC News"
    },
    "author": "null",
    "title": "Ukraine says N Korea troops likely pulled from front line over heavy losses - BBC.com",
    "description": "Western officials say North Koreans have suffered heavy losses since being sent to fight for Russia.",
    "url": "https://www.bbc.com/news/articles/cjder8zgk48o",
    "urlToImage": "https://ichef.bbci.co.uk/news/1024/branded_news/91f9/live/7ae55db0-dfed-11ef-a819-277e390a7a08.jpg",
    "publishedAt": "2025-01-31T17:01:32Z",
    "content": "James Waterhouse\r\nUkrainian special forces fighting in Russia's western Kursk region have told the BBC they have not seen any North Korean troops there for the past three weeks. \r\nA spokesman said it… [+2186 chars]"
  },
  {
    "source": {
      "id": "abc-news",
      "name": "ABC News"
    },
    "author": "ABC News",
    "title": "Federal employees told to remove pronouns from email signatures by end of day - ABC News",
    "description": "null",
    "url": "https://abcnews.go.com/US/federal-employees-told-remove-pronouns-email-signatures-end/story?id\\\\u003d118310483",
    "urlToImage": "null",
    "publishedAt": "2025-01-31T16:43:42Z",
    "content": "null"
  }
]

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


list_of_dict = []
for d in json_data:
    list_of_dict.append(flatten_json(d))
    
fieldnames = list_of_dict[0].keys()
writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
writer.writeheader()
writer.writerows(list_of_dict)





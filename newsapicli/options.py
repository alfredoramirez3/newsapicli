from enum import Enum


class CategoryOption(str, Enum):
    business = "business"
    entertainment = "entertainment"
    general = "general"
    health = "health"
    science = "science"
    sports = "sports" 
    technology = "technology" 
 
   
class OutputOption(str, Enum):
    csv = "csv"
    json = "json"
    table = "table"
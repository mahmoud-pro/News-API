import requests as r
# from bs4 import BeautifulSoup
from dotenv import dotenv_values, load_dotenv
import os

load_dotenv()
config = dotenv_values(".env")
api_key = os.getenv("API_KEY")

url = f"https://newsapi.org/v2/everything?q=tesla&from=2023-02-23&sortBy=publishedAt&apiKey={api_key}"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 "
                  "Safari/537.36"
}

res = r.get(url, headers=headers)
content = res.json()

for article in content["articles"]:
    print(article["title"])
    print(article["description"])



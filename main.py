import requests as r
from send_email import send_email
from dotenv import dotenv_values, load_dotenv
import os

load_dotenv()
config = dotenv_values(".env")
api_key = os.getenv("API_KEY")

url = f"https://newsapi.org/v2/everything?q=tesla&from=2023-02-28&sortBy=publishedAt&apiKey={api_key}"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 "
                  "Safari/537.36"
}

res = r.get(url, headers=headers)
content = res.json()

print(content)

body = ""

for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2 * "\n"


body = body.encode("utf-8")
send_email(body)

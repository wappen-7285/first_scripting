import requests
from bs4 import BeautifulSoup

url = "https://tsunishi.jp/"
res = requests.get(url)
soup = BeautifulSoup(res.content, "html.parser")

articles = []

for a in soup.find_all("a"):
    title = a.text.strip()
    link = a.get("href")

    if title and link:
        articles.append({
            "title": title,
            "link" : link
        })

for article in articles:
    print(article["title"])
    print(article["link"])
    print("-" * 20)
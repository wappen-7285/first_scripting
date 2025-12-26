import requests
from bs4 import BeautifulSoup

def fetch_ariticles(url):
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
    return articles

url = "https://www.mie-takada-hj.ed.jp/hj4/"
articles = fetch_ariticles(url)
for a in articles:
    print(a)
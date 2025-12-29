import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_url = "https://www.tsuko.ed.jp/"
relative = "info/school_event/entry-979.html"


res = requests.get(base_url)
soup = BeautifulSoup(res.content, "html.parser")

articles = []

for a in soup.find_all("a"):
    title = a.text.strip()
    link = a.get("href")

    if not title or not link:
        continue

    full_url = urljoin(base_url, link)
    articles.append({"title": title, "url" : full_url})

clean = []
seen = set()

for a in articles:
    url = a["url"]

    if url.startswith("javascript"):
        continue
    if url in seen:
        continue

    seen.add(url)
    clean.append(a)

for clean in clean:
    print(clean["title"],clean["url"])
    print("-" * 20)
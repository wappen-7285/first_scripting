import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_url = "https://www.kuwana-h.ed.jp/top.html"

res = requests.get(base_url)
res.raise_for_status()

soup = BeautifulSoup(res.content, "html.parser")

links = soup.find_all("a")
results = []

for a in links:
    title = a.text.strip()
    link = a.get("href")

    if not title or not link:
        continue
    if link.startswith("javascript"):
        continue

    full_url = urljoin(base_url, link)
    results.append({"title": title, "url": full_url})

for item in results:
    
    print(item["title"], item["url"])
    print("-" * 20)
 

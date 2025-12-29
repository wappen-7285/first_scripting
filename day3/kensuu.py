import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from collections import defaultdict

base_url = "https://www.tsuko.ed.jp/"

KEYWORDS = ["入試", "行事", "お知らせ"]

def analyze(title):
    return any(k in title for k in KEYWORDS)

def fetch_url(url):
    try:
        res = requests.get(url, timeout=5)
        res.raise_for_status()
        return res
    except requests.exceptions.RequestException:
        print("取得失敗", url)
        return None

res = fetch_url(base_url)
if res is None:
    exit()

soup = BeautifulSoup(res.content, "html.parser")

articles = soup.find_all("a")

data = []
seen = set()

for a in articles:
    title = a.get_text(strip=True)
    link = a.get("href")

    if not title or not link:
        continue
    if link.startswith("javascript"):
        continue

    full_url = urljoin(base_url, link)

    if full_url in seen:
        continue

    seen.add(full_url)
    data.append({"title": title, "url": full_url})


filtered = [a for a in data if analyze(a["title"])]

count = len(filtered)
print(f"該当記事数: {count}件です。")

stats = defaultdict(int)

for a in filtered:
    for k in KEYWORDS:
        if k in a["title"]:
            stats[k] += 1

print(dict(stats))
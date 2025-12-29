import sys
print(sys.executable)

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [4, 5, 6])
plt.show()


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

def json_save(data, filename):
    with open(filename, "w" , encoding = "utf-8") as f:
        json.dump(data, f, ensure_ascii = False, indent = 2)

def json_load(filename):
    with open(filename, encoding="utf-8") as f:
        return json.load(f)

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

json_save(filtered, "filtered.json")

stats = {}
for k in KEYWORDS:
    stats[k] = sum(k in a["title"] for a in filtered)

labels = list(stats.keys())
values = list(stats.values())

plt.bar(labels, values)
plt.title("カテゴリー別件数")
plt.xlabel("カテゴリー")
plt.ylabel("件数")
plt.show()
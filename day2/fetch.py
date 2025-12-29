import requests

def fetch_url(url):
    try:
        res = requests.get(url, timeout = 5)
        res.raise_for_status()
        return res
    except requests.RequestException as e:
        print("取得失敗", url)
        return None
    

res = fetch_url("https://www.tsuko.ed.jp/")
if res is None:
    exit()
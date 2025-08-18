# Link Verification - Download linked pages in page.

from bs4 import BeautifulSoup
import requests

URL = "https://automatetheboringstuff.com/2e/chapter12/"
res = requests.get(URL)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")
links = soup.find_all("a")

for link in links:
    follow_url = str(link.get("href"))  # type:ignore
    if follow_url.startswith("http"):
        print(f"Downloading page {follow_url}")
        try:
            res = requests.get(follow_url)
            res.raise_for_status()
        except requests.exceptions.HTTPError as e:
            if res.status_code == 404:
                print(f"Broken link (404): {follow_url}")
            else:
                print(f"Other HTTP error for {follow_url}: {e}")

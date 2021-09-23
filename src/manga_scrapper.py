# JJ Small
# Scrapes data from MangaUpdates

from bs4 import BeautifulSoup
import requests

url = "https://www.mangaupdates.com/series.html?id="
series = ["111447", "151847", "112459", "114562", "15", "111445", "111123"]
data = []

for s in series:
    print(f"getting manga title {s}")
    r = requests.get(url=f"{url}{s}")
    r.raise_for_status()
    content = r.text
    print(f"Web page size = {len(r.content)}")

    data.append(BeautifulSoup(r.content, "html.parser"))

for manga in data:
    title = manga.find(name="span", class_="releasestitle tabletitle")
    content = manga.find_all("div", class_="sContent")

    source_volumes = content[6].text.strip("\n")
    english_volumes = content[24].text.strip("\n")

    print(title.text)
    print(source_volumes)
    print(english_volumes)

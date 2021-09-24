# JJ Small
# Scrapes data from MangaUpdates
from bs4 import BeautifulSoup
import requests

def series_search(manga_title):
    """
    Grabs the first search result of the given manga title
    
    Parameters:
        manga_title (string): The name of the series to search for

    Returns:
        TODO: Will eventually return series info if match found, else returns null or something...
    """

    r = requests.post("https://mangaupdates.com/search.html", params={"search": manga_title})
    soup = BeautifulSoup(r.text, "html.parser")

    series_section = soup.find("div", id="main_content").find_all("div", class_="row")

    try:
        first_match = series_section[1].find("div", class_="col-6 py-1 py-md-0 text")
    except IndexError:
        print("No result found...")
    else:
        name = first_match.text
        i_id = first_match.a["href"].replace(
                        "https://www.mangaupdates.com/series.html?id=", ""
                    )
        print(f"{name} - {i_id}")

def scratch_work():
    url = "https://www.mangaupdats.com/series.html?id="
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
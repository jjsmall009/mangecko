# JJ Small
# Scrapes data from MangaUpdates
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz, process
import re
import requests

def search_scrapper(manga_title):
    """
    Finds the most likely match from the list of series in the series section using the
    FuzzyWuzzy module. If the series with the highest score is over the threshold than we 
    assume that it's the correct series and proceed from there.
    
    Parameters:
        manga_title (string): The name of the series to search for

    Returns:
        ID (int): The mangaupdates ID for a series, or -1 if no match is found
    """

    r = requests.post("https://mangaupdates.com/search.html", params={"search": manga_title})
    soup = BeautifulSoup(r.text, "html.parser")

    try:
        series_section = soup.find("div", id="main_content"
                            ).find(text="Series Info"
                            ).findNext("div")
    except AttributeError:
        print("No results found for this series")
    else:
        section_rows = series_section.findAll(name="div", 
            class_=["col-6 py-1 py-md-0 text", "col-6 py-1 py-md-0 text alt"])

        titles = [t.text for t in section_rows]

        # ### Do some fuzzy testing
        # print("\nRatio testing\n------------------")
        # for title in titles:
        #     print(f"{manga_title} -> {title} = {fuzz.ratio(manga_title, title)}")

        # print("\nPartial ratio testing\n------------------------")
        # for title in titles:
        #     print(f"{manga_title} -> {title} = {fuzz.partial_ratio(manga_title, title)}")

        # print("\nToken ratio\n---------------------")
        # for title in titles:
        #     print(f"{manga_title} -> {title} = {fuzz.token_sort_ratio(manga_title, title)}")

        # print("\nExtract all\n----------------")
        # print(process.extract(manga_title, titles))

        potential_match = process.extractOne(manga_title, titles)
   
        # We now have to scan through the series section again to tie the match to the series info
        if int(potential_match[1]) >= 90:
            final_match = None
            for row in section_rows:
                title = row.find(name="a", text=potential_match[0])
                if title != None:
                    final_match = title

            name = final_match.text
            i_id = final_match["href"].replace(
                            "https://www.mangaupdates.com/series.html?id=", ""
                        )
            print(f"{manga_title} -> {name} - {i_id}")
            return int(i_id)
        else:
            print(f"No suitable result found for {manga_title}")
            return -1
            

def series_scrapper(manga_id):
    """
    Grabs data from the specified mangaupdates ID

    Parameters:
        manga_id (int): ID for a mangaupdates.com series

    Returns:
        TODO: This will return something at some point
    """

    url = f"https://www.mangaupdates.com/series.html?id={manga_id}"
    r = requests.get(url=url)

    series_section = BeautifulSoup(r.content, "html.parser").find("div", id="main_content")
    content = series_section.find_all("div", class_="sContent")

    title = series_section.find(name="span", class_="releasestitle tabletitle").text
    source_section = content[6].text.strip("\n")
    english_section = content[24].text.strip("\n")
    source_volumes = re.search(r'\d+', source_section).group()
    english_volumes = re.search(r'\d+', english_section).group()
    
    print(title)
    print(f"\tSource = {source_section}")
    print(f"\tResult = {source_volumes}")
    print(f"\tEnglish = {english_section}")
    print(f"\tResult = {english_volumes}\n")


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

    # Fuzzy string finding tests
    best_match = [-1, -1]
    for title in possible_titles:
        ratio = fuzz.token_sort_ratio(manga_title, title.text)
        print(f"{title.text} - {ratio}")
        if ratio > best_match[0]:
            best_match[0] = ratio
            best_match[1] = title
        
    if best_match[0] > 80:
        name = best_match[1].text
        i_id = best_match[1].a["href"].replace(
                        "https://www.mangaupdates.com/series.html?id=", ""
                    )
        print(f"{name} - {i_id}")
    else:
        print(f"No suitable result found for {manga_title}")
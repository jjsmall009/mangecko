# JJ Small
# Scrapes data from MangaUpdates
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz, process
import re
import requests
import time
import bs4

def series_search(title):
    """
    Wrapper function to search for a series. Will try and do this concurrently to speed up requests

    Parameters:
        manga_list (dict): Title/volumes
    
    Returns:
        series_ids (list): List of mangaupdates ID for each matching series
    """

    while True:
        try:
            id = search(title)
        except Exception as e:
            print(e)
            print(f"---> Too many attempts. Failed to search for {title}. Retrying.\n")
            time.sleep(1)
        else:
            if id != None:
                return id
            else:
                return None
            break


def search(manga_title):
    """
    Finds the most likely match from the list of series in the series section using the
    FuzzyWuzzy module. If the series with the highest score is over the threshold than we 
    assume that it's the correct series and proceed from there.
    
    Parameters:
        manga_title (string): The name of the series to search for

    Returns:
        ID (int): The mangaupdates ID for a series, or -1 if no match is found
    """

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
    r = requests.get("https://mangaupdates.com/series.html", 
                    params={"search": manga_title, "output":"json"}, 
                    headers=headers)

    results = r.json()["results"]["items"]
    titles = [t["title"] for t in results]

    potential_match = process.extractOne(manga_title, titles)

    if potential_match[1] >= 90:
        index = titles.index(potential_match[0])
        id = int(results[index]["id"])
        return id
    else:
        print(f"---> No match for -> {manga_title}")
        return None
            

def series_scraper(manga_id, obj):
    """
    Grabs data from the specified mangaupdates ID

    Parameters:
        manga_id (int): ID for a mangaupdates.com series

    """
    print(f"scraping {manga_id}")

    while True:
        try:
            url = f"https://www.mangaupdates.com/series.html?id={manga_id}"
            r = requests.get(url=url)
        except Exception as e:
            print(f"---> Studid connection error on {manga_id}... Retrying")
            time.sleep(1)
        else:
            series_section = BeautifulSoup(r.content, "html.parser").find("div", id="main_content")
            content = series_section.find_all("div", class_="sContent")

            obj.site_title = series_section.find(name="span", class_="releasestitle tabletitle").text
            
            obj.source_status, obj.source_volumes = get_source_info(content)

            obj.eng_status, obj.eng_volumes = get_english_info(content)

            if "Yes" in content[23].text:
                obj.is_licensed = True
            else:
                obj.is_licensed = False

            obj.year = int(content[20].text.strip("\n"))

            break


def get_source_info(content_section):
    source_section = [m.strip("\n") for m in content_section[6] if type(m) is bs4.element.NavigableString]
    source_volumes = None

    try:
        source_volumes = int(re.search(r'\d+', source_section[0]).group())
    except AttributeError:
        print("No source???")

    if ("Complete" or "Completed") in source_section[0]:
        status = "Complete"
    elif "Ongoing" in source_section[0]:
        status = "Ongoing"
    elif ("Cancelled" or "Canceled") in source_section[0]:
        status = "Cancelled"
    elif "Hiatus" in source_section[0]:
        status = "Hiatus"
    else:
        status = "Unknown"

    return status, source_volumes


def get_english_info(content_section):
    """
    The english source section can have multiple publishers and volume counts. The criteria is that
    the publisher with the largest volume count is most likely the one we want so sort the lines in
    the section and grab data from the first line.
    """

    english_section = [m.strip("\n") for m in content_section[24] if type(m) is bs4.element.NavigableString and m != "\n"]
    english_section.sort()
    eng_status, eng_volumes = None, None

    try:
        eng_volumes = int(re.search(r'\d+', english_section[0]).group())
        #obj.eng_status = "Complete" if "Complete" in english_section else "Ongoing"
        if ("Complete" or "Completed") in english_section[0]:
            eng_status = "Complete"
        elif "Ongoing" in english_section[0]:
            eng_status = "Ongoing"
        elif ("Cancelled" or "Canceled") in english_section[0]:
            eng_status = "Cancelled"
        elif "Hiatus" in english_section[0]:
            eng_status = "Hiatus"
        elif "Dropped" in english_section[0]:
            eng_status = "Dropped"
        else:
            eng_status = "Unknown"
    except AttributeError:
        print(f"\t---> Attribute error: No english volumes")
    except IndexError:
        print("\t---> Index Error: No english volumes")

    return eng_status, eng_volumes
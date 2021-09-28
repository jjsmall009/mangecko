# JJ Small
# Scrapes data from MangaUpdates
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz, process
import re
import requests
import time

def search_scrapper(title):
    """
    Wrapper function to search for a series. Will try and do this concurrently to speed up requests

    Parameters:
        manga_list (dict): Title/volumes
    
    Returns:
        series_ids (list): List of mangaupdates ID for each matching series
    """

    series_id = -1
    while True:
        try:
            id = search(title)
        except Exception as e:
            print(e)
            print(f"---> Fail on {title}. Retrying.\n")
            time.sleep(2)
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
        print(f"{manga_title} -> {potential_match[0]} -> ID = {id}")
        return id
    else:
        print(f"No match for -> {manga_title}")
        return None
            

def series_scrapper(manga_id, obj):
    """
    Grabs data from the specified mangaupdates ID

    Parameters:
        manga_id (int): ID for a mangaupdates.com series

    Returns:
        TODO: This will return something at some point
    """

    while True:
        try:
            url = f"https://www.mangaupdates.com/series.html?id={manga_id}"
            r = requests.get(url=url)
        except Exception as e:
            print(f"Studid connection error in SERIES SCRAPPER....")
            time.sleep(2)
        else:
            series_section = BeautifulSoup(r.content, "html.parser").find("div", id="main_content")
            content = series_section.find_all("div", class_="sContent")

            obj.site_title = series_section.find(name="span", class_="releasestitle tabletitle").text
            source_section = content[6].text.strip("\n")
            english_section = content[24].text.strip("\n")

            obj.source_status = "Complete" if "Complete" in source_section else "Ongoing"
            obj.source_volumes = int(re.search(r'\d+', source_section).group())

            try:
                obj.eng_volumes = int(re.search(r'\d+', english_section).group())
                obj.eng_status = "Complete" if "Complete" in source_section else "Ongoing"
            except AttributeError:
                print("\tNo english license")

            break
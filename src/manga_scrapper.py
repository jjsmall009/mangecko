# JJ Small
# Scrapes data from MangaUpdates
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz, process
import re
import requests
import time

def search_scrapper(manga_list):
    """
    Executes searches for the given list of manga titles

    Parameters:
        manga_list (dict): Title/volumes
    
    Returns:
        series_ids (list): List of mangaupdates ID for each matching series
    """
    series_ids = []
    for manga in manga_list:
        while True:
            try:
                id = search(manga)
            except Exception as e:
                print(e)
                print(f"---> Fail on {manga}. Retrying.\n")
                time.sleep(2)
            else:
                if id > 0:
                    series_ids.append(id)
                print()
                break

    return series_ids


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
        return -1
            

def series_scrapper(manga_id):
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

            title = series_section.find(name="span", class_="releasestitle tabletitle").text
            source_section = content[6].text.strip("\n")
            english_section = content[24].text.strip("\n")

            source_status = "Complete" if "Complete" in source_section else "Ongoing"
            source_volumes = re.search(r'\d+', source_section).group()

            try:
                english_volumes = re.search(r'\d+', english_section).group()
                english_status = "Complete" if "Complete" in source_section else "Ongoing"
            except AttributeError:
                print("\tNo english license")
                english_volumes = "N/a"
                english_status = "N/a"

            print(title)
            print(f"\tSource Status: {source_status} - Source volumes = {source_volumes}")
            print(f"\tEnglish Status: {english_status} - English volumes = {english_volumes}")

            break
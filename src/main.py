#################################################################################################
"""Manga Volume Tracker

Author: JJ Small
Date: September 2021

main.py
Description:
    This main script acts as a collection manager for the directory you want to scan. For each valid
    folder(series) it finds it will create a Manga object and update the information about it.
Output:
    The output is the various lists of data. Valid series, invalid series, manga with matching 
    results, etc.
"""
#################################################################################################
from dir_scanner import DirectoryScanner
from manga_scrapper import search_scrapper, series_scrapper
from manga import Manga
from pathlib import Path
import db_manager
import time

start = time.time()

# For a given path there are a few kinds of data we're working with
# - Dict of valid series (key:value = series name: local volume count)
# - List of invalid series (don't contain any volumes, aren't organized correctly, etc.)
# - List of Manga objects (series that are found, not found, etc.)
path = Path("D:\Manga\TEST_FILES")
valid_series = {}
invalid_series = []
manga = []

scanner = DirectoryScanner(path)
scanner.scan_directory()
valid_series = scanner.valid_folders
invalid_series = scanner.invalid_folders

scanner.print_valid()
scanner.print_invalid()

# For each valid folder, create a Manga object and then get some precious data
for series, vol_count in valid_series.items():
    current_manga = Manga(series, vol_count)
    id = search_scrapper(series)

    if id != None:
        current_manga.id = id
        current_manga.has_match = True
        series_scrapper(id, current_manga)

    manga.append(current_manga)

# Output all of the data we have to let the user know how things went
print("\n========================\nSeries with no matches")
[manga.print_no_match() for manga in manga if manga.has_match == False]

print("\n======================\nSeries with matches")
[manga.print_has_match() for manga in manga if manga.has_match == True]

for manga in manga:
    if manga.eng_volumes != None:
        if manga.my_volumes < manga.eng_volumes:
            print(f"{manga.local_title} has new volumes")

#####################################
# Database testing

conn = db_manager.create_connection("data\TEST_FILES")
db_manager.create_table(conn, "manga")
db_manager.add_data(conn)


print(f"Elapsed time = {time.time() - start}")
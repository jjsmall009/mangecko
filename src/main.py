# JJ Small
# main.py
# For now this serves as the hub for testing the features of my program as they appear
from dir_scanner import DirectoryScanner
from manga_scrapper import search_scrapper, series_scrapper
from pathlib import Path
from fuzzywuzzy import fuzz, process

path = Path("D:\Manga\TEST_FILES")
scanner = DirectoryScanner(path)
scanner.scan_directory()
scanner.print_scanner_results()

# print("Search Results...\n=================")
# series_IDs = []
# for manga in scanner.valid_folders:
#     ID = search_scrapper(manga)
#     if ID > 0:
#         series_IDs.append(ID)
#     print()

series_scrapper(88303)
series_scrapper(149641)
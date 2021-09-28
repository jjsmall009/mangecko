# JJ Small
# main.py
# For now this serves as the hub for testing the features of my program as they appear
from dir_scanner import DirectoryScanner
from manga_scrapper import search_scrapper, series_scrapper, search
from pathlib import Path
import time

path = Path("D:\Manga\TEST_FILES")
scanner = DirectoryScanner(path)
scanner.scan_directory()
scanner.print_scanner_results()

print("Search Results...\n=================")
ids = search_scrapper(scanner.valid_folders)
print(len(ids))  

print("Grabbing series data...\n==============================")
for id in ids:
    series_scrapper(id)
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

print("Search Results...\n=================")
for manga in scanner.valid_folders:
    search_scrapper(manga)
    print()
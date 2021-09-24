# JJ Small
# main.py
# For now this serves as the hub for testing the features of my program as they appear
from dir_scanner import scan_folder, print_volume_info
from manga_scrapper import series_search
from pathlib import Path
from fuzzywuzzy import fuzz, process

print("Time to party")

path = Path("D:\Manga\TEST_FILES")
folder_data = scan_folder(path)

print("Scan results....\n================")
print_volume_info(folder_data)

print("Search Results...\n=================")
for manga in folder_data:
    series_search(manga)
    print()
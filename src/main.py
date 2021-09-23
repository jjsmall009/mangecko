from dir_scanner import scan_folder, print_volume_info
from manga_scrapper import series_search
from pathlib import Path

print("Time to party")

path = Path("D:\Manga\TEST_FILES")
folder_data = scan_folder(path)

for manga in folder_data:
    series_search(manga)

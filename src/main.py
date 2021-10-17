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
from library_scanner import LibraryScanner
from manga_scrapper import search_scrapper, series_scrapper
from manga import Manga
from pathlib import Path

import db_manager
import time


def add_library():
    path = Path(input("\t-> Path to directory: "))

    if not Path(path).exists():
        print("Invalid path...")
        return

    scanner = LibraryScanner(path)
    scanner.scan_directory()

    if len(scanner.valid_folders) == 0:
        print("No folders founds. Not a valid library. Exiting...")
        return
    else:
        print(f"\tThis library has {len(scanner.valid_folders)} series.")
        choice = input("\tAdd this library and continue? (y/n): ")

    
opening_header = """============================
Welcome to Manga Manager 1.0
============================"""

options="""
Options:
    * 1: Add a Library
    * 2: Scan a Library
    * 3: Update Volume Info
    * 4: View New Volumes
    * 5: Exit
"""

# Initialize our database and setup our connection
db_manager.create_database()

print(opening_header, end="")
while True:
    print(options)
    choice = input("Enter a choice: ")

    if choice == "1":
        add_library()

    elif choice == "2":
        # get path and scan directory for file changes
        pass
    elif choice == "3":
        # get library and grab new volume data from api
        pass
    elif choice == "4":
        # get some data and print it out
        pass
    elif choice == "5":
        print("Happy reading!")
        break
    else:
        print("Invalid input. Try again...")
    

start = time.time()

# For a given path there are a few kinds of data we're working with
# - Dict of valid series (key:value = series name: local volume count)
# - List of invalid series (don't contain any volumes, aren't organized correctly, etc.)
# - List of Manga objects (series that are found, not found, etc.)
# path = Path("D:\Manga\TEST_FILES")
# valid_series = {}
# invalid_series = []
# manga = []

# scanner = LibraryScanner(path)
# scanner.scan_directory()
# valid_series = scanner.valid_folders
# invalid_series = scanner.invalid_folders

# scanner.print_valid()
# scanner.print_invalid()

# # For each valid folder, create a Manga object and then get some precious data
# for series, vol_count in valid_series.items():
#     current_manga = Manga(series, vol_count)
#     id = search_scrapper(series)

#     if id != None:
#         current_manga.site_id = id
#         current_manga.has_match = True
#         series_scrapper(id, current_manga)

#     manga.append(current_manga)

# # Output all of the data we have to let the user know how things went
# print("\n========================\nSeries with no matches")
# [manga.print_no_match() for manga in manga if manga.has_match == False]

# print("\n======================\nSeries with matches")
# [manga.print_has_match() for manga in manga if manga.has_match == True]

# for manga in manga:
#     if manga.eng_volumes != None:
#         if manga.my_volumes < manga.eng_volumes:
#             print(f"{manga.local_title} has new volumes")

# #####################################
# # Database testing

# conn = db_manager.create_connection("data\TEST_FILES")
# db_manager.create_table(conn, "manga")
# db_manager.add_data(conn)


# print(f"Elapsed time = {time.time() - start}")
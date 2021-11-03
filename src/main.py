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
    """
    A library is just a collection of folders that are related to one another (Completed, Ongoing, Favorites, Raw, etc.)

    A library in the database stores info about all matching series in the folder, even ones that don't have a MangaUpdates match.
    """

    path = Path(input("\t-> Path to directory: "))

    if not Path(path).exists():
        print("Invalid path...")
        return

    scanner = LibraryScanner(path)
    scanner.scan_directory()
    valid_series = scanner.valid_folders
    manga = []

    if len(scanner.valid_folders) == 0:
        print("No folders founds. Not a valid library. Exiting...")
        return
    else:
        print(f"\tThis library has {len(scanner.valid_folders)} series.")
        choice = input("\tAdd this library and continue? (y/n): ")

        if choice == "y":
            if not db_manager.insert_library(path.name, str(path)):
                return

            # For each valid folder, create a Manga object and then get some precious data
            for series, vol_count in valid_series.items():
                current_manga = Manga(series, vol_count)
                id = search_scrapper(series)

                if id != None:
                    current_manga.site_id = id
                    current_manga.has_match = True
                    series_scrapper(id, current_manga)

                manga.append(current_manga)

            db_manager.insert_manga(manga, path.name)


def choose_library():
    libraries = db_manager.get_libraries()

    for l in libraries:
        print(f"\t{l[0]}: {l[1]}")

    choice = int(input("\tWhich library do you want to scan?: "))
    if choice not in [l[0] for l in libraries]:
        print("Not a valid library. Try again...")
        return -1
    else:
        return choice


def scan_library():
    """
        1. Before getting here, this is tested for valid library name/path
        2. For each folder in this library
            a. Are you in the database?
                1. Yes, update my_volume count and move on
                2. No, 
                    a. create Manga object
                    b. Query api for data
                    c. Add manga entry to database
        3. For each row in database for this library
            a. Are you stored locally?
                1. Yes, carry on
                2. No, delete from junction table
            
    """
    library_id = choose_library()

    if library_id == -1:
        print("No libraries in database")
        return
    else:
        path = Path(db_manager.get_library_path(library_id))
        scanner = LibraryScanner(path)
        scanner.scan_directory()
        valid_series = scanner.valid_folders
        manga = []

        for series, vol_count in valid_series.items():
            has_match = db_manager.series_exists(series, library_id)
            if has_match:
                print(f"{series} -> you exist")
                db_manager.update_volume_info(series, vol_count)
            else:
                print("you are dead...")
                current_manga = Manga(series, vol_count)
                id = search_scrapper(series)

                if id != None:
                    current_manga.site_id = id
                    current_manga.has_match = True
                    series_scrapper(id, current_manga)

                manga.append(current_manga)
        db_manager.insert_manga(manga, path.name)

def update_library():
    library_id = choose_library()
    if library_id == -1:
        return
        
    # Query DB and get ongoing series
    ongoing_series = db_manager.get_ongoing(library_id)

    # Series tuple = (local_title, my_volumes, site_id)
    for series in ongoing_series:
        current_manga = Manga(series[0], series[1])
        current_manga.site_id = series[2]

        series_scrapper(series[2], current_manga)

        db_manager.update_manga(current_manga)


def find_new_volumes():
    """Query the DB for series with local volumes < english or source volumes"""

    library_id = choose_library()

    if library_id == -1:
        print("No libraries in database")
        return
    else:
        series = db_manager.series_with_new_volumes(library_id)

        for s in series:
            print(f"{s[0]:<50} Volume {s[1]} -> Volume {s[2]}")


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
        scan_library()
    elif choice == "3":
        update_library()
    elif choice == "4":
        find_new_volumes()
    elif choice == "5":
        print("Happy reading!")
        break
    else:
        print("Invalid input. Try again...")
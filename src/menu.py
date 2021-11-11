from library_scanner import LibraryScanner
from manga_scraper import series_search, series_scraper
from manga_model import Manga
from pathlib import Path
import database_manager

opening_header = "============================\n" + \
                 "Welcome to Manga Manager 1.0\n" + \
                 "============================"

options = """
Options:
    * 1: Add a Library
    * 2: Scan a Library
    * 3: Update Volume Info
    * 4: View New Volumes
    * 5: Exit 
"""

def add_library():
    """
    A library is just a collection of series that are related to one another 
    (Completed, Ongoing, Favorites, Raw, etc.)

    A library in the database stores info about all matching series in the folder, 
    even ones that don't have a MangaUpdates match.
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
            if not database_manager.insert_library(path.name, str(path)):
                return

            # For each valid folder, create a Manga object and then get some precious data
            for series, vol_count in valid_series.items():
                current_manga = Manga(series, vol_count)
                id = series_search(series)

                if id != None:
                    current_manga.site_id = id
                    current_manga.has_match = True
                    series_scraper(id, current_manga)

                manga.append(current_manga)

            database_manager.insert_manga(manga, path.name)


def choose_library():
    libraries = database_manager.get_libraries()

    if len(libraries) == 0:
        print("No libraries in database...")
        return

    for l in libraries:
        print(f"\t{l[0]}: {l[1]}")

    try:
        choice = int(input("\tWhich library do you want to scan?: "))

        if choice not in [l[0] for l in libraries]:
            print("Not a valid library. Try again...")
            return
        else:
            return choice
    except Exception:
        print("Invalid input. Try again later...")

def scan_library(): 
    library_id = choose_library()

    if not library_id:
        return

    path = Path(database_manager.get_library_path(library_id))
    scanner = LibraryScanner(path)
    scanner.scan_directory()
    valid_series = scanner.valid_folders
    manga = []

    for series, vol_count in valid_series.items():
        has_match = database_manager.series_exists(series, library_id)
        if has_match:
            database_manager.update_volume_info(series, vol_count)
        else:
            print(f"New series added -> {series}")
            current_manga = Manga(series, vol_count)
            id = series_search(series)

            if id != None:
                current_manga.site_id = id
                current_manga.has_match = True
                series_scraper(id, current_manga)

            manga.append(current_manga)
    database_manager.insert_manga(manga, path.name)

    db_series = database_manager.get_series(library_id)
    for series in db_series:
        if series not in valid_series:
            print(f"Deleting {series}...")
            database_manager.delete_series(series)

def update_library():
    library_id = choose_library()

    if not library_id:
        return

    # Query DB and get ongoing series
    ongoing_series = database_manager.get_ongoing(library_id)

    # Series tuple = (local_title, my_volumes, site_id)
    for series in ongoing_series:
        current_manga = Manga(series[0], series[1])
        current_manga.site_id = series[2]

        series_scraper(series[2], current_manga)

        database_manager.update_manga(current_manga)


def find_new_volumes():
    """Query the DB for series with local volumes < english or source volumes"""

    library_id = choose_library()

    if not library_id:
        return
        
    series = database_manager.series_with_new_volumes(library_id)

    for s in series:
        print(f"{s[0]:<50} Volume {s[1]} -> Volume {s[2]}")


def menu_loop():
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
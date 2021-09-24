# JJ Small
# Manga Volume Tracker
# dir_scanner.py - Code to scan a directory and get a list of manga title/volume count
from pathlib import Path

FILE_EXT = (".cbz", ".cbr", ".zip", ".pdf")

def scan_folder(path):
    """
    Scans the specified folder and returns each manga title and how many volumes there are.
    
    Parameters:
        path (Path object or string): Path of the directory to scan.

    Returns:
        dict: title/volume count of each series found.
    
    Notes:
        Ignores standalone files and empty directories.
    """

    manga_folders = [folder for folder in path.iterdir() if folder.is_dir()]
    manga_volume_info = {}

    for manga in manga_folders:
        volumes = [vol for vol in manga.iterdir() if vol.suffix in FILE_EXT]
        if len(volumes) > 0:
            manga_volume_info[manga.name.split(" [", 1)[0]] = len(volumes)
        else:
            print(manga.name)

    return manga_volume_info

def print_volume_info(manga_dict):
    """Helper function to print out the contents of the scanned directory"""

    for title, volumes in manga_dict.items():
        print(f"{title} - {volumes} volumes")
    print(f"There are {len(manga_dict)} series\n")
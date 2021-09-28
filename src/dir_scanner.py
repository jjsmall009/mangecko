# JJ Small
# Manga Volume Tracker
# dir_scanner.py - Code to scan a directory and get a list of manga title/volume count
from pathlib import Path

class DirectoryScanner():
    """
    This is a class because it's easier to track the state of which folder in the directory is what.
    
    """
    FILE_EXT = (".cbz", ".cbr", ".zip", ".pdf")

    def __init__(self, path):
        self.path = path
        self.valid_folders = {}
        self.invalid_folders = []

    def scan_directory(self):
        """
        Scans the specified folder and returns each manga title and how many volumes there are.
        
        Parameters:
            path (Path object or string): Path of the directory to scan.

        Returns:
            dict: title/volume count of each series found.
        
        Notes:
            Ignores standalone files and empty directories.
        """

        manga_folders = [folder for folder in self.path.iterdir() if folder.is_dir()]

        for manga in manga_folders:
            volumes = [vol for vol in manga.iterdir() if vol.suffix in self.FILE_EXT]
            if len(volumes) > 0:
                self.valid_folders[manga.name.split(" [", 1)[0]] = len(volumes)
            else:
                self.invalid_folders.append(manga.name)

    def print_scanner_results(self):
        """Helper function to print out the contents of the scanned directory"""

        print(f"\nResults for {self.path}\n=============================================")

        print("Invalid folders - Folders that don't meet the criteria")
        for folder in self.invalid_folders:
            print(f"\t{folder}")

        print("Valid folders - These are the manga series found in this directory")
        for title, volumes in self.valid_folders.items():
            print(f"\t{title} - {volumes} volumes")
        print(f"There are {len(self.valid_folders)} valid series\n")
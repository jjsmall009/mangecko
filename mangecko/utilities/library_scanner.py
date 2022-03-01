# JJ Small
# Manga Volume Tracker
# library_scanner.py - Code to scan a directory and get a list of manga title/volume count
from pathlib import Path

class LibraryScanner():
    """
    This is a class because it's easier to track the state of which folder in the directory is what.
    """
    FILE_EXT: tuple = (".cbz", ".cbr", ".zip", ".pdf")

    def __init__(self, path: Path) -> None:
        self.path = path
        self.valid_folders: dict[str, int] = {}
        self.invalid_folders: list[str] = []

    def scan_directory(self) -> None:
        """
        Scans the specified folder and finds each manga title and how many volumes there are.
        
        Notes:
            Ignores standalone files and empty directories. I.e, folder with stuff in them.
        """

        manga_folders: list[Path] = [folder for folder in self.path.iterdir() if folder.is_dir()]

        for manga in manga_folders:
            num_volumes = 0 #[vol for vol in manga.iterdir() if vol.suffix in self.FILE_EXT]
            for vol in manga.iterdir():
                if vol.suffix in self.FILE_EXT:
                    num_volumes += 1

            if num_volumes > 0:
                self.valid_folders[manga.name.split(" [", 1)[0]] = num_volumes
            else:
                self.invalid_folders.append(manga.name)

    def print_valid(self) -> None:
        """Helper function to print out the valid folders"""

        print("\n==================================================================")
        print("Valid folders - These are the manga series found in this directory")
        for title, volumes in self.valid_folders.items():
            print(f"\t{title} - {volumes} volumes")

        print(f"There are {len(self.valid_folders)} valid series")

    def print_invalid(self) -> None:
        """Helper function to print out the invalid foldesr"""

        print("\n=======================================================")
        print("Invalid folders - Folders that don't meet the criteria")
        for folder in self.invalid_folders:
            print(f"\t{folder}")

        print(f"There are {len(self.invalid_folders)} invalid series")
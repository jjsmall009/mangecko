# JJ Small
# Manga Volume Tracker
# dir_scanner.py - Code to scan a directory and get a list of manga title/volume count
import os

path_name = "D:\Manga\Short Manga"
root_dir = os.scandir(path_name)

# Traverse one level down for each folder in the path and count how many volumes there are
series_volumes = {}
file_ext = (".cbz", ".cbr", ".zip")
for series in root_dir:
    if series.is_dir():
        current_path = os.path.join(path_name, series.name)
        current_dir = os.scandir(current_path)
        volume_count = 0
        for volume in current_dir:
            if volume.is_file():
                if volume.name.endswith(file_ext):
                    volume_count += 1

        # A series has to has at least 1 valid volume
        if volume_count > 0:
            series_volumes[series.name] = volume_count

for title, volumes in series_volumes.items():
    print(f"{title} - {volumes} volumes")

print(len(series_volumes))
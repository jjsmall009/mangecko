# Overall Idea

> This program (working title: Manga Manager) is a visual reflection of the folders and files that a person has stored locally on their computer.

Each library added to the program is a folder that contains other folders of manga.

## Program Components

1. Library Scanning
    - This program treats a top level folder/directory as a "library". That is, the subfolders of the top level folder are manga series.
    - To add a library to the program, give it a path to the directory and it will scan for valid subfolders.
    - The important pieces of information is a series title and the number of volumes for that series.
2. Web Scrapping
    - Once a library has been scanned we need to get information from MangaUpdates about each series.
    - This includes official title, source status and volumes, english status and volumes, things like that.
    - Values that don't have any matching data will be null.
3. Database Management
    - The database stores library and manga information, as well as the relationship between them.
    - A library has many manga entries and a manga entry can be in many libraries (will work on that as well as custom library filters later...).
    - The junction table between the library and manga table is just the ID of both.

## Data I Want from MangaUpdates

The whole crux of this program is to get an accurate english volume count for each series. That way the program can scan a library, pull in new data for ongoing series, and let yo know which series have new volumes.

- Series ID
- Series title from page
- Status in Country of Origin
  - \# of volumes
- Complete, Ongoing, Cancelled, etc.
- Licensed (in English)
  - Yes, No, Dropped
- English Publisher
  - \# of Volumes (greatest)
  - Complete, Ongoing, N/A
- Authors
- Years

## Phase 1 - Menu Based Interface

Eventually this will be full fledged GUI app but for now the first implementation will be a console app. The menu below gives an idea of the features and functionality for phase one.

```
============================
Welcome to Manga Manager 1.0
============================
Options:
  * 1: Add a Library
  * 2: Scan a Library
  * 3: Update Library
  * 4: Find New Volumes
  * 5: Exit
```

**1. Add a Library** - Specify a path and the program will scan the directory, find valid series, pull data for each series, and add all of the data to the database.
**2. Scan a Library** - Display a list of libraries. Pick one. It will then scan the directory for said library and look for changes (new series, removed series, new volumes for a series).
**3. Update a Library** - Display a list of libraries. Pick one. For series marked as ongoing, grab new data and update the database.
**4. Find New Volumes** - Simply query the database for a library and print out series that have local_volumes < english_volumes.

Now, some of the options might get combined or use bits and pieces of each other.

### Some User Stories

- Getting a list of new volumes
  1. "Scan a Library" to check for changes to local files.
  2. "Update a Library" to get new data for ongoing series (or mark as complete).
  3. "Find New Volumes" to grab data from the database and print out a list.  
  
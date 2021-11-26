# Manga Volume Tracker

## Overview

I've been mulling over this project for a few years now and I've finally decided to finally give it a go.

I have quite the collection of manga on my computer and it's pretty time consuming and cumbersome to keep track of when a new volume in a series comes out. My goal is to create a program that will maintain a database of the manga I have and query some API to determine which series have new volumes.

There's still a lot to decide and design but in general this is some of the ideas I have and some of the features I intend to implement.

- Nice UI. The main view will be a grid of images/titles for a series. Cover, name, etc.
- You can click on a series to bring up some basic info about it.
- There will be a button to scan through your series and check if any new volumes are out (it won't download anything, just let you know there's something new).
- Specify different "shelves" based on some sort of criteria. Completed series, favorites, etc.

## Potential UI

![UI mockup](resources/mockup1.PNG)

## A Note on File Organization

Like most media trackers/scanners/organization tools there is list of criteria that is necessary to follow in order to properly find files and folders.

1. Each series must be in its own folder.
    * Series name should be as accurate as possible without any extra things at the end.
2. Volumes should be named as cleanly as possible (Series title, volume number).
    * Bonus volumes, extras, etc., should be in their own folder. Still working on handling this.

As of now I don't do any sort of volume filename parsing to accurately count the total number of volumes. Right now it just looks for the filename extension and counts those up.

- Extensions: .cbr, .cbz, .zip, and PDF

## Tech Stack

After a couple of months I'm pretty well ingrained in the following:

- Python
- PyQT / PySide6
- SQLite

It will be a pretty basic CRUD app but I want to focus on the look and feel, responsiveness, and good software engineering principles and design.

## Current Progress

### Stage 3 - Clean Up

- [ ] Refactor and clean up my code.
- [ ] Add in loading bars or spinners.
- [ ] Improve UI and polish up the look and feel.
- [ ] Create a flow based layout for the series grid.

### Stage 2 - GUI

- [x] Do some initial layout planning and GUI mockups.
- [x] Learn the basics of PyQt (PySide6 actually).
- [x] Get started with Qt Designer.
- [x] Organize files.
- [x] Integrate layout with the rest of my code.
- [ ] Work on proper logging.

### Stage 1 - Console Based Menu

- [x] Create a basic design doc of ideas and program features.
- [x] Take a look at which API has what I want.
- [x] Start iterating and do one small task at a time and build.
- [x] Fuzzy string matching.
- [x] Grab series data for each valid search result.
- [x] Compare volume results
- [x] Test some database functionality and design.
- [x] Implement console menu design.

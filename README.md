# Mangecko

## Overview - Version 1.0

Mangecko is a manga cataloging program to visually keep track of your digital manga collection (still a WIP).

![Main screen](resources/main_screen.PNG)

## How to Use

Most features are working as intended but there's still a lot of work to do.

1. Run "mangecko.py" to launch the application.
2. Click on "Add Library" and follow the steps.
3. To update a library, use the buttons on the top left. Scan Library -> Update Library -> New Volumes.

## A Note on File Organization

Like most media trackers/scanners/organization tools there is list of criteria that is necessary to follow in order to properly find files and folders.

1. Each series must be in its own folder.
    * Series name should be as accurate as possible without any extra things at the end.
2. Volumes should be named as cleanly as possible (Series title, volume number).
    * Bonus volumes, extras, etc., should be in their own folder. Still working on handling this.

As of now I don't do any sort of volume filename parsing to accurately count the total number of volumes. Right now it just looks for the filename extension and counts those up.

* Extensions: .cbr, .cbz, .zip, and PDF

## Tech Stack

This project uses the following:

* Python
* PyQT / PySide6
* SQLite

### Big todo...

Mangaupdates has since created an API you can use so when I have the time to dive back into this project I'll have to do a rewrite to use it.
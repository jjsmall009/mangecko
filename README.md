# Manga Volume Tracker

## Overview

I've been mulling over this project for a few years now and I've finally decided to finally give it a go.

I have quite the collection of manga on my computer and it's pretty time consuming and cumbersome to keep track of when a new volume in a series comes out. My goal is to create a program that will maintain a database of the manga I have and query some API to determine which series have new volumes.

There's still a lot to decide and design but in general this is some of the ideas I have and some of the features I intend to implement.

- Nice UI. The main view will be a grid of images/titles for a series. Cover, name, etc.
- You can click on a series to bring up some basic info about it.
- There will be a button to scan through your series and check if any new volumes are out (it won't download anything, just let you know there's something new).
- Specify different "shelves" based on some sort of criteria. Completed series, favorites, etc.

## Tech Stack

I still have some research to do on which manga API I'll be using but here's the tech.

- Python
- PyQT (still up in the air on the best/easiest Python GUI)
- SQLite

It will be a pretty basic CRUD app but I want to focus on the look and feel, responsiveness, and good software engineering principles and design.

## Next Steps

This readme will be a working document to keep track of what I'm doing and what I need to next.

- [ ] Create a basic design doc of ideas and program features.
- [ ] Take a look at which API has what I want.
- [ ] Start iterating and do one small task at a time and build.

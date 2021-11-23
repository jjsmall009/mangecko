"""Manga Volume Tracker

Author: JJ Small
Date: November 2021

main.py
Description:
    Clean and simple. Runs the main menu loop.
"""
from models import database_manager
from controllers import menu

def main():
    # Initialize our database and setup our connection
    database_manager.create_database()

    menu.menu_loop()

if __name__ == "__main__":
    main()
# Manage a database of manga??? Not sure what I'm doing
import sqlite3

def create_database():
    """First time running the program create the database"""
    try:
        with sqlite3.connect("data\manga_library.db"):
            print("Database created successfully.")
    except sqlite3.Error as e:
        print(e)

def database_exists():
    return

def create_connection(database_name):
    """Connects to database or creates it if not found"""
    conn = None
    try:
        conn = sqlite3.connect(database_name)
        return conn
    except sqlite3.Error as e:
        print(e)

    return conn

def create_table(conn, table_name):
    """Creates a table for a library of manga"""

    statement = """CREATE TABLE IF NOT EXISTS manga (
                        id INTEGER PRIMARY KEY,
                        local_title TEXT NOT NULL,
                        site_title TEXT,
                        has_match TEXT,
                        manga_id INTEGER,
                        my_volumes INTEGER NOT NULL,
                        source_volumes INTEGER,
                        source_status TEXT,
                        eng_volumes INTEGER,
                        eng_status TEXT);
                """
    try:
        c = conn.cursor()
        c.execute(statement)
    except sqlite3.Error as e:
        print(e)


def add_data(conn):
    """Adds a row to the table if it doesn't already exist in said table"""
    
    statement = """
                insert into manga 
                    (local_title, has_match, manga_id, my_volumes, eng_status) values
                    ("Dragon ball", True, 123, 16, "Complete");
    
    """

    cur = conn.cursor()
    cur.execute(statement)

    statement = """
                insert into manga 
                    (local_title, site_title, has_match, manga_id, my_volumes, eng_status) values
                    ("Aho-Girl", "Aho Girl", True, 123, 16, "Complete");
    
    """
    cur.execute(statement)


    conn.commit()


# Manage a database of manga??? Not sure what I'm doing
import sqlite3

db_path = "data\manga_library.db"

def create_database():
    """First time running the program create the database"""
    try:
        with sqlite3.connect(db_path) as conn:
            libraries_table = """CREATE TABLE IF NOT EXISTS libraries (
                                    library_id INTEGER PRIMARY KEY,
                                    library_name TEXT,
                                    path_name TEXT);

                """
            create_table(conn, libraries_table)

            manga_table = """CREATE TABLE IF NOT EXISTS manga_series (
                                id INTEGER PRIMARY KEY,
                                local_title TEXT NOT NULL,
                                site_title TEXT,
                                site_id INTEGER,
                                my_volumes INTEGER NOT NULL,
                                eng_volumes INTEGER,
                                eng_status TEXT
                                source_volumes INTEGER,
                                source_status TEXT,
                                has_match TEXT);
                """
            create_table(conn, manga_table)

            junction = """CREATE TABLE IF NOT EXISTS library_manga (
                            library_id INTEGER,
                            manga_id INTEGER,
                            FOREIGN KEY(library_id) REFERENCES libraries(library_id),
                            FOREIGN KEY(manga_id) REFERENCES manga(id));
                """
            create_table(conn, junction)
            
            print("Database created successfully.")
    except sqlite3.Error as e:
        print(e)


def create_table(conn, statement):
    """Creates a table for a library of manga"""

    try:
        c = conn.cursor()
        c.execute(statement)
    except sqlite3.Error as e:
        print(e)


def create_connection():
    """Connects to database or creates it if not found"""

    conn = None
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except sqlite3.Error as e:
        print(e)

    return conn


def insert_library(name, path):
    with create_connection() as conn:
        statement = """INSERT INTO libraries (library_name, path_name) VALUES (?, ?);"""

        cur = conn.cursor()
        cur.execute(statement, (name, path))
        conn.commit()


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


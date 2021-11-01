# JJ Small
# The database manager is a set of functions that manipulates the database, obviously.
import sqlite3

db_path = "data\manga_library.db"

def create_connection():
    """Connects to database or creates it if not found"""

    conn = None
    try:
        conn = sqlite3.connect(db_path)
        conn.execute("""PRAGMA foreign_keys = ON""")
        return conn
    except sqlite3.Error as e:
        print(e)


def create_database():
    """First time running the program create the database"""

    try:
        with create_connection() as conn:
            libraries_table = """CREATE TABLE IF NOT EXISTS libraries (
                                    library_id INTEGER PRIMARY KEY,
                                    library_name TEXT UNIQUE,
                                    path_name TEXT);

                """
            create_table(conn, libraries_table)

            manga_table = """CREATE TABLE IF NOT EXISTS manga_series (
                                id INTEGER PRIMARY KEY,
                                local_title TEXT NOT NULL,
                                site_title TEXT,
                                site_id INTEGER,
                                my_volumes INTEGER NOT NULL,
                                is_licensed TEXT,
                                eng_volumes INTEGER,
                                eng_status TEXT,
                                source_volumes INTEGER,
                                source_status TEXT,
                                has_match TEXT,
                                year INTEGER);
                """
            create_table(conn, manga_table)

            junction = """CREATE TABLE IF NOT EXISTS library_manga (
                            library_id INTEGER,
                            manga_id INTEGER,
                            FOREIGN KEY(library_id) REFERENCES libraries(library_id) ON DELETE CASCADE,
                            FOREIGN KEY(manga_id) REFERENCES manga_series(id) ON DELETE CASCADE);
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


def insert_library(name, path):
    """A library is a collection of related manga series"""

    try:
        with create_connection() as conn:
            statement = """INSERT INTO libraries (library_name, path_name) VALUES (?, ?);"""

            cur = conn.cursor()
            cur.execute(statement, (name, path))
            conn.commit()
            return True
    except sqlite3.IntegrityError:
        print("Library already exists. Moving on...")
        return False


def insert_manga(manga_list, library_name):
    """
    In order to maintain good data integrity we use a junction table to connect a manga
    to a library. That is, a library has many manga and a manga can be in many libraries.
    """

    with create_connection() as conn:
        cur = conn.cursor()
        find_library = """SELECT library_id from libraries WHERE library_name = ?;"""
        cur.execute(find_library, [library_name])
        library_id = cur.fetchall()[0][0]

        for manga in manga_list:
            statement = """INSERT INTO manga_series (local_title,site_title,site_id,my_volumes,
                                                    is_licensed,eng_volumes,eng_status,source_volumes,
                                                    source_status,has_match,year) 
                                
                                VALUES (?,?,?,?,?,?,?,?,?,?,?);"""

            data = (manga.local_title,manga.site_title,manga.site_id,manga.my_volumes,
                    manga.is_licensed,manga.eng_volumes,manga.eng_status,manga.source_volumes, 
                    manga.source_status,manga.has_match,manga.year)
            cur.execute(statement, data)
            
            last_manga_id = cur.lastrowid

            junction = """INSERT INTO library_manga VALUES (?,?);"""
            cur.execute(junction, (library_id, last_manga_id))

            conn.commit()


def get_libraries():
    try:
        with create_connection() as conn:
            cur = conn.cursor()
            cur.execute("""SELECT library_id, library_name from libraries""")

            return cur.fetchall()
    except sqlite3.Error as e:
        print(f"Error in getting libraries ---> {e}")


def get_ongoing(library_id):
    try:
        with create_connection() as conn:
            cur = conn.cursor()
            statement = """SELECT manga_series.local_title, manga_series.my_volumes, manga_series.site_id 
                            FROM manga_series
                            INNER JOIN library_manga
                            ON manga_series.id = library_manga.manga_id
                            WHERE library_manga.library_id = ?
                            AND (manga_series.eng_status = \"Ongoing\"
                                OR manga_series.eng_status = \"Hiatus\"
                                OR manga_series.source_status = \"Ongoing\"
                                OR manga_series.source_status = \"Hiatus\")"""

            cur.execute(statement, (library_id,))

            return cur.fetchall()
    except sqlite3.Error as e:
        print(f"Error in getting ongoing series ---> {e}")


def update_manga(manga):
    """Update new data for things we care about"""

    try:
        with create_connection() as conn:
            cur = conn.cursor()
            statement = """UPDATE manga_series
                            SET is_licensed=?,eng_volumes=?,eng_status=?,source_volumes=?,source_status=?
                            WHERE site_id = ?"""

            data = (manga.is_licensed, manga.eng_volumes, manga.eng_status,
                    manga.source_volumes, manga.source_status, manga.site_id)

            cur.execute(statement, data)

            conn.commit()
    except sqlite3.Error as e:
        print(f"Error in updating manga ---> {e}")


def series_with_new_volumes(library_id):
    """
    The main focus is series that have an official translation in English, but we fall back
    onto checking the original Japanese source if there isn't an English version.
    """

    try:
        with create_connection() as conn:
            cur = conn.cursor()
            results = []
            statement = """SELECT manga_series.local_title, manga_series.my_volumes, manga_series.eng_volumes
                            FROM manga_series
                            INNER JOIN library_manga
                            ON manga_series.id = library_manga.manga_id
                            WHERE library_manga.library_id = ?
                            AND manga_series.my_volumes < manga_series.eng_volumes
                            AND manga_series.eng_volumes IS NOT NULL
                            """

            cur.execute(statement, (library_id,))

            results += cur.fetchall()

            statement = """SELECT manga_series.local_title, manga_series.my_volumes, manga_series.source_volumes
                            FROM manga_series
                            INNER JOIN library_manga
                            ON manga_series.id = library_manga.manga_id
                            WHERE library_manga.library_id = ?
                            AND manga_series.my_volumes < manga_series.source_volumes
                            AND manga_series.eng_volumes IS NULL
                            """

            cur.execute(statement, (library_id,))

            results += cur.fetchall()

            return results
    except sqlite3.Error as e:
        print(f"Error in doing volume stuff ---> {e}")


def delete_test():
    with create_connection() as conn:
        cur = conn.cursor()
        cur.execute("""DELETE FROM manga_series WHERE id = 9""")
        conn.commit()
        print("Deleted manga series #9")
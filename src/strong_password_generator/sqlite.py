import sqlite3
from sqlite3 import Error

DATABASE_PATH = "./sqlite/db/database.db"

def start_database():
    conn = create_connection()

    if conn is not None:
        # create Passwords table
        create_table(conn, passwords_table())
    else:
        print("Error! cannot create the database connection.")

def create_connection(db_file = DATABASE_PATH):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql) -> None:
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def passwords_table() -> str:
    return """ CREATE TABLE IF NOT EXISTS passwords (
        id integer PRIMARY KEY,
        site_name text NOT NULL,
        site_url text NOT NULL,
        email text NOT NULL,
        password text NOT NULL,
        created_at text
    ); """

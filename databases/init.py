import psycopg2
from psycopg2 import Error
from config import DATABASE_NAME, DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_PORT

create_table("A1", "nouns")
create_table("A1", "verbs")
create_table("A1", "adjectives")

create_table("A2", "nouns")
create_table("A2", "verbs")
create_table("A2", "adjectives")

create_table("B1", "nouns")
create_table("B1", "verbs")
create_table("B1", "adjectives")

create_table("B2", "nouns")
create_table("B2", "verbs")
create_table("B2", "adjectives")

create_table("C1", "nouns")
create_table("C1", "verbs")
create_table("C1", "adjectives")

create_table("C2", "nouns")
create_table("C2", "verbs")
create_table("C2", "adjectives")

def create_table(level, kind):
    try:
        db_connection = connect_db()
        cursor = db_connection.cursor()
    except(Error):
        print("[Error]: ", Error)
        return 1

    table = f"{level}_{kind}_words"
    
    cursor.execute(f'''
                    CREATE TABLE IF NOT EXISTS {table} (
                    id serial PRIMARY KEY,
                    word VARCHAR(64) UNIQUE NOT NULL,
                    transcription VARCHAR(64),
                    translation VARCHAR(64) NOT NULL,
                    definition TEXT(4096));
                    ''')
    
    db_connection.commit()
    db_connection.close()


def connect_db():
    return psycopg2.connect(database=DATABASE_NAME, username=DATABASE_USERNAME, 
                            password=DATABASE_PASSWORD, host=DATABASE_HOST, 
                            port=DATABASE_PORT)

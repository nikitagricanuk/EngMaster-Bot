import psycopg2
from psycopg2 import Error
from config import DATABASE_NAME, DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_PORT

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

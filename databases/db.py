import psycopg2
from psycopg2 import Error

def insert_word(word, transcription, translation, definition, table):
    try:
        db_connection = connect_db()
        cursor = db_connection.cursor()
    except(Error):
        print("[Error]: ", Error)
    
    cursor.execute(f'''
                    INSERT INTO {table} (word, transcription, translation, definition)
                    VALUES ('{word}', '{transcription}', '{translation}', '{definition}');
                    ''')
    
    db_connection.commit()
    db_connection.close()

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
    return psycopg2.connect(database='words', username='engmaster', 
                            password='cabeiMoh4Pah', host='postgresql', 
                            port='5432')

#!/usr/bin/python3

from bs4 import BeautifulSoup
import psycopg2
from psycopg2 import Error
import time

start_tm = time.time()

DATABASE_NAME = "engmaster"
DATABASE_USERNAME = "engmaster"
DATABASE_PASSWORD = "cabeiMoh4Pah"
DATABASE_HOST = "postgres"
DATABASE_PORT = 5432

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

def connect_db():
    return psycopg2.connect(database=DATABASE_NAME, user=DATABASE_USERNAME, 
                            password=DATABASE_PASSWORD, host=DATABASE_HOST, 
                            port=DATABASE_PORT)

for levels in ["A1", "A2", "B1", "B2", "C1", "C2"]:
    for kind in ["adjectives", "nouns", "verbs", "adverbs"]:
        name = f"words_{levels}_{kind}"

        with open(f"content/{name}.html") as fp:
            soup = BeautifulSoup(fp, 'html.parser')

        table = soup.find('table')

        for row in table.find_all('tr'):
            columns = row.find_all('td')
            print(f'{columns[0].text} {columns[1].text} {columns[2].text}')

            db_connection = connect_db()
            cursor = db_connection.cursor()
            
            cursor.execute(f'''
                            INSERT INTO {name} (word, transcription, translation)
                            VALUES ('{columns[0].text}', '{columns[1].text}', '{columns[2].text}');
                            ''')
            
            db_connection.commit()
            db_connection.close()

end_tm = time.time()

print("done (", end_tm - start_tm, ")")
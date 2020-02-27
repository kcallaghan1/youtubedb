#!/usr/bin/python
 
import psycopg2
import random
import string
from config import config
from random_word import RandomWords


def insert_url(url_name):
    """ insert a new url into the urls table """
    sql = """INSERT INTO URLs (videoId, url) VALUES(%s,%s) RETURNING videoId;"""
    conn = None
    videoId = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (url_name),)
        # get the generated id back
        videoId = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
    return videoId

possibleCharacters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
characters = []
for j in range(64):
    characters.append(possibleCharacters[j:j+1])

for i in range(100000):
    url = ""
    for j in range(11):
        letter = random.choice(characters)
        url += letter
    url_to_insert = (i, url)
    insert_url(url_to_insert)
    #print(url_to_insert)

print("Done!")

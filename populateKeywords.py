#!/usr/bin/python
 
import psycopg2
import random
import string
from config import config
from random_word import RandomWords


def insert_keyword(keyword_name):
    """ insert a new keyword into the keywords table """
    sql = """INSERT INTO Keywords (videoId, keyword) VALUES(%s,%s) RETURNING videoId;"""
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
        cur.execute(sql, (keyword_name),)
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

words = []

f = open("Words.txt", "r")

for i in range(3251):
    #print(f.readline())
    word = f.readline()
    words.append(word[0:len(word)-1])

ten = []

for i in range(10):
    ten.append(i)

for i in range(100000):
    content = ""
    for j in range(random.choice(ten)):
        content += random.choice(words)
        content += ", "
    content += random.choice(words)
    keyword_to_insert = (i, content)
    insert_keyword(keyword_to_insert)
    #print(url_to_insert)

print("Done!")

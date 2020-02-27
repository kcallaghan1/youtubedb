#!/usr/bin/python
 
import psycopg2
import random
import string
from config import config

words = []

f = open("Words.txt", "r")

for i in range(3251):
    #print(f.readline())
    word = f.readline()
    words.append(word[0:len(word)-1])

def generateChannelName():
    name = random.choice(words) + random.choice(words)
    return name

def insert_channel(channel_name):
    """ insert a new channel into the channels table """
    sql = """INSERT INTO Channels (channelId, channelName) VALUES(%s,%s) RETURNING channelId;"""
    conn = None
    channelId = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (channel_name),)
        # get the generated id back
        channelId = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
    return channelId

for i in range(100000):
    name = generateChannelName()
    channel_to_insert = (i, name)
    insert_channel(channel_to_insert)


print("Done!")

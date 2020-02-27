#!/usr/bin/python
 
import psycopg2
import random
import string
from config import config

def insert_view(view_name):
    """ insert a new view into the views table """
    sql = """INSERT INTO PlaylistVideos (playlistId, videoId) VALUES(%s,%s) RETURNING playlistId;"""
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
        cur.execute(sql, (view_name),)
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

numbers = []

for i in range(100000):
    numbers.append(i)

days = []
for i in range(31):
    days.append(i+1)

months = []
for i in range(12):
    months.append(i+1)

years = []
for i in range(2005, 2020):
    years.append(i+1)


for i in range(100000):
    channel = random.choice(numbers)
    video = random.choice(numbers)
    view_to_insert = (channel, video)
    insert_view(view_to_insert)
    #print(view_to_insert)


print("Done!")

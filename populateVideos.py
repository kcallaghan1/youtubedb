#!/usr/bin/python
 
import psycopg2
import random
import string
from config import config

def insert_video(video_name):
    """ insert a new video into the videos table """
    sql = """INSERT INTO Videos (videoId, channelId, title, description, duration, categoryId, thumbnail, year, month, day) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING videoId;"""
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
        cur.execute(sql, (video_name),)
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
    years.append(i)

categories = []
for i in range(15):
    categories.append(i+1)

for i in range(100000):
    channel = random.choice(numbers)
    video = i
    title = ""
    for i in range(random.choice([1, 2, 3, 4, 5])):
        title += random.choice(words)
        title += " "
    title += random.choice(words)
    duration = random.choice(days) * random.choice(months)
    description = ""
    for i in range(random.choice(days)):
        description += random.choice(words)
        description += " "
    description += random.choice(words)
    thumbnail = bytes(random.choice(months))
    year = random.choice(years)
    month = random.choice(months)
    category = random.choice(categories)
    day = random.choice(days)
    if(day == 31 and (month == 4 or month == 6 or month == 9 or month == 11)):
       day = 30
    if(day == 31 and month == 2):
        if(year == 2008 or year == 2012 or year == 2016):
            day = 29
        else:
            day = 28
    video_to_insert = (video, channel, title, description, duration, category, thumbnail, year, month, day)
    insert_video(video_to_insert)
    #print(video_to_insert)


print("Done!")

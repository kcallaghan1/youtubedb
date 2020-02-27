#!/usr/bin/python
 
import psycopg2
import random
import string
from config import config

def insert_comment(comment_name):
    """ insert a new comment into the comments table """
    sql = """INSERT INTO Comments (commentId, channelId, videoId, content, year, month, day) VALUES(%s,%s,%s,%s,%s,%s,%s) RETURNING channelId;"""
    conn = None
    commentId = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (comment_name),)
        # get the generated id back
        commentId = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
    return commentId

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
    years.append(i+1)


for i in range(100000):
    channel = random.choice(numbers)
    video = random.choice(numbers)
    year = random.choice(years)
    month = random.choice(months)
    day = random.choice(days)
    content = ""
    for j in range(random.choice(months)):
        content += random.choice(words)
        content += " "
    content += random.choice(words)
    if(day == 31 and (month == 4 or month == 6 or month == 9 or month == 11)):
       day = 30
    if(day == 31 and month == 2):
        if(year == 2008 or year == 2012 or year == 2016):
            day = 29
        else:
            day = 28
    comment_to_insert = (i, channel, video, content, year, month, day)
    insert_comment(comment_to_insert)
    #print(view_to_insert)


print("Done!")

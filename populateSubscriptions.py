#!/usr/bin/python
 
import psycopg2
import random
import string
from config import config

def insert_subscription(subscription_name):
    """ insert a new subscription into the subscriptions table """
    sql = """INSERT INTO Subscriptions (channelId, subscribedChannel) VALUES(%s,%s) RETURNING channelId;"""
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
        cur.execute(sql, (subscription_name),)
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

for i in range(100000):
    channel1 = random.choice(numbers)
    channel2 = random.choice(numbers)
    subscription_to_insert = (channel1, channel2)
    insert_subscription(subscription_to_insert)
    #print(subscription_to_insert)


print("Done!")

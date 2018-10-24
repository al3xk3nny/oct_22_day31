# The below demonstrates inserting multiple lines of data into a table called "Friends". You could also use a For Loop to achieve this, but it is not advised as it creates alot of network traffic - i.e. multiple trips back and forth to the server.

import os
import datetime
import pymysql

connection = pymysql.connect(host='localhost',
                             user=os.getenv('C9_USER'),
                             password='',
                             db='Chinook')

try:
    with connection.cursor() as cursor:
        rows = [("bob", 21, "1990-02-06 23:04:56"),
                ("jim", 56, "1955-05-09 13:12:45"),
                ("fred", 100, "1911-09-12 01:01:01")]
        cursor.executemany("INSERT INTO Friends VALUES (%s,%s,%s);", rows)
        connection.commit()
finally:
    connection.close()
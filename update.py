# The below demonsrates an update to the table called "Friends" where "bob's" age is updated from 21 to 22.

import os
import pymysql

connection = pymysql.connect(host='localhost',
                             user=os.getenv('C9_USER'),
                             password='',
                             db='Chinook')
try:
    with connection.cursor() as cursor:
        cursor.execute("UPDATE Friends SET age = 22 WHERE name = 'bob';")
        connection.commit()
finally:
    connection.close()
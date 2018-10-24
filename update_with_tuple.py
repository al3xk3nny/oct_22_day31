# The below also demonstates an update, but uses a tuple to affect it. This is a better option then the other update scenario.

import os
import pymysql

connection = pymysql.connect(host='localhost',
                             user=os.getenv('C9_USER'),
                             password='',
                             db='Chinook')
try:
    with connection.cursor() as cursor:
        cursor.execute("UPDATE Friends SET age = %s WHERE name = %s;",
                       (23, 'bob'))
        connection.commit()
finally:
    connection.close()
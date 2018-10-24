# Installing a library for Python to talk to mySql database;
# sudo pip3 install --upgrade setuptools
# sudo pip3 install pymysql

# The below simply demonstrates selecting data from a table. The data returns as a tuple of tuples.

import os
import pymysql

username = os.getenv('C9_USER')

connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()
import pymysql
import os

username = os.environ.get("C9_USER")


connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM Album"
        cursor.execute(sql)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
finally:
    connection.close()
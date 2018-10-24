from flask import Flask, render_template, request
import pymysql
import os


app = Flask(__name__)


@app.route("/")
def show_index():
    return render_template("index.html")

    
@app.route("/search")
def search():
    connection = pymysql.connect(host='localhost',
                             user=os.environ.get("C9_USER"),
                             password='',
                             db='Chinook')
    
    try:
        query = "%" + request.args["q"] + "%"
        
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT * FROM Artist WHERE Name like %s"
            cursor.execute(sql, query)
            rows = cursor.fetchall()
    
            for row in rows:
                print(row)

        return render_template("artist_list.html", artists=rows)
    finally:
        connection.close()    


@app.route("/artist/<int:id>")
def artist_detail(id):
    connection = pymysql.connect(host='localhost',
                             user=os.environ.get("C9_USER"),
                             password='',
                             db='Chinook')
    
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT * FROM Artist WHERE ArtistId = %s"
            cursor.execute(sql, id)
            artists = cursor.fetchone() # Returns a dictionary with one item. "fetchall" would have returned a list with a dictionary with one item.
        
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT * FROM Album WHERE ArtistId = %s"
            cursor.execute(sql, id)
            rows = cursor.fetchall()
    
            for row in rows:
                print(row)

        return render_template("artist_detail.html", artist=artists, albums=rows)
    finally:
        connection.close() 


@app.route("/album/<int:id>")
def album_detail(id):
    connection = pymysql.connect(host='localhost',
                             user=os.environ.get("C9_USER"),
                             password='',
                             db='Chinook')
    
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT * FROM Album WHERE AlbumId = %s"
            cursor.execute(sql, id)
            albums = cursor.fetchone()
        
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT * FROM Track WHERE AlbumId = %s"
            cursor.execute(sql, id)
            rows = cursor.fetchall()
    
            for row in rows:
                print(row)

        return render_template("album_detail.html", album=albums, tracks=rows)
    finally:
        connection.close() 


if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)
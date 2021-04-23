from flask import Flask, request, render_template
import psycopg2
import random
import flask

app = Flask(__name__)

def get_db_length():
    try:
        connection = psycopg2.connect(user="aisi",
                                    password="aisi",
                                    host="postgres",
                                    port="5432",
                                    database="aisi_notes")
        print("Connecting with", connection)
        cursor = connection.cursor()
        print("Searching note", id)
        postgreSQL_select_Query = "select count(*) from notes;"
        cursor.execute(postgreSQL_select_Query)
        mobile_records = cursor.fetchall()

        return mobile_records[0][0]

    except (Exception, psycopg2.Error) as error:
        return("Error")

@app.route("/")
def hello():
    random_entry = str(random.randint(1,get_db_length()))
    url_path = "http://localhost:8080/db/" + random_entry
    print(url_path)
    return render_template('index.html', url_path=url_path, entry=random_entry)

@app.route("/db/<id>")
def get_db(id):
    try:
        connection = psycopg2.connect(user="aisi",
                                    password="aisi",
                                    host="postgres",
                                    port="5432",
                                    database="aisi_notes")
        print("Connecting with", connection)
        cursor = connection.cursor()
        print("Searching note", id)
        postgreSQL_select_Query = "select * from notes where note_id=" + id + ";"
        cursor.execute(postgreSQL_select_Query)
        mobile_records = cursor.fetchall()

        entry = mobile_records[0][0],mobile_records[0][1]

        return render_template('show.html', entry=entry, url_path = "http://localhost:8080/")

    except (Exception, psycopg2.Error) as error:
        return("Error")

if __name__ == '__main__':
    app.run()

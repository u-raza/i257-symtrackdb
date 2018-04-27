import sqlite3

from flask import Flask, render_template, url_for, request, redirect
# for keeping track of user sessions
from flask import session, escape, flash
# to override url_for
import os
# interaction with database
import models

app = Flask(__name__)

@app.route('/')
def index():
    # create tables in database

    # create patient table
    models.create_patient_table()
    return render_template('index.html')

@app.route('/contact-us')
def contact():
    return render_template('contactus.html')

@app.route('/patient')
def patient():
    conn = sqlite3.connect('i257symtrack.db')
    c = conn.cursor()
    data = []
    query = """SELECT patient_id, name, date_of_birth, street_address, city, state, country, telephone FROM patient"""
    for db_row in c.execute(query):
        data_row = {}
        data_row["patient_id"] = db_row[0]
        data_row["name"] = db_row[1]
        data_row["date_of_birth"] = db_row[2]
        data_row["street_address"] = db_row[3]
        data_row["city"] = db_row[4]
        data_row["state"] = db_row[5]
        data_row["country"] = db_row[6]
        data_row["telephone"] = db_row[7]
    data.append(data_row)
    return render_template("patient.html", data=data)


# Workaround for updating static files even when
# the browser caches old files.
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)
##### end browser cache fix


@app.route('/patient', methods=['GET'])
def view_table_patient():
    conn = sqlite3.connect('i257symtrack.db')
    c = conn.cursor()
    data = []
    query = """SELECT patient_id, name, date_of_birth, street_address, city, state, country, telephone FROM patient"""
    for db_row in c.execute(query):
        data_row = {}
        data_row["patient_id"] = db_row[0]
        data_row["name"] = db_row[1]
        data_row["date_of_birth"] = db_row[2]
        data_row["street_address"] = db_row[3]
        data_row["city"] = db_row[4]
        data_row["state"] = db_row[5]
        data_row["country"] = db_row[6]
        data_row["telephone"] = db_row[7]
    data.append(data_row)
    return render_template("patient.html", data=data)


if __name__ == "__main__":
    app.run()
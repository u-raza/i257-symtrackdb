import sqlite3

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def hello_flask():
    return 'Hello Flask!'

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
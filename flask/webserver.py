import sqlite3

from flask import Flask, render_template, url_for, request, redirect
# for keeping track of user sessions
from flask import session, escape, flash
# to override url_for
import os
# interaction with database
import models
# forms and validation
from forms import PatientForm, QueryForm


app = Flask(__name__)

# form validation
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contact-us')
def contact():
    return render_template('contactus.html')

# show patient list
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
    conn.close()
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


#### app routes for dummy data
# add patient and other data
@app.route('/setup', methods=['GET', 'POST'])
def setup():
    pform = PatientForm()
    #return redirect('/login')
    error = None
    if pform.validate_on_submit():

        #user input
        name = pform.name.data
        dob = pform.dob.data
        street = pform.street_address.data
        city = pform.city.data
        state = pform.state.data
        country = pform.country.data
        telephone = pform.telephone.data

        patient = models.add_patient(name, dob, street, city, state, country, telephone)

        error = 'A patient with that patient id already exists'
        return redirect('/patient')
    return render_template('setup.html', error = error, form = pform)

@app.route('/fill_symptoms', methods=['GET', 'POST'])
def fill_symptoms():
    # sym_id = 3
    # name = 'testing'
    # models.add_symptom(sym_id, name, 'blah', False, False, True, False)
        
    with open('data/symptoms_dummydata_only.csv') as fin:
        lines = fin.readlines()
        for line in lines:
            lst = line.split(',')
            if len(lst) == 2:
                sym_id, name = lst
            else:
                sym_id, name, _ = lst
            #print(line)
            # Add symptom, giving it a severity
            try:
                models.add_symptom(sym_id, name, name, False, False, True, False)
            except:
                print(sym_id, name)

    return render_template('index.html')


@app.route('/submit_queries', methods=['GET', 'POST'])
def submit_queries():
    qform = QueryForm()
    error = None
    if qform.validate_on_submit():
        #user input
    #     id = qform.id.data
    #     sdate = qform.start_date.data
    #     edate = qform.end_date.data
    #     q = qform.query_type.data

    #     query = models.submit_query(id, sdate, edate, q)

    #     error = 'A patient with that patient id already exists'
    #     return redirect('/submit_queries')
        return render_template('queries.html')
    return render_template('queries.html', error = error, form = qform)

if __name__ == "__main__":
    app.run()






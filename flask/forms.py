
# from flask.ext.wtf import Form // this is deprecated
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SelectField, DateField, RadioField
# from flask_wtf.html5 import EmailField // this is deprecated
from wtforms.fields.html5 import EmailField
from wtforms import validators
import sqlite3

# patient sign up form
class PatientForm(FlaskForm):
    name = StringField('name', [validators.required()])
    dob = StringField('dob', [validators.required()])
    street_address = StringField('street_address', [validators.required()])
    city = StringField('city', [validators.required()])
    state = StringField('state', [validators.required()])
    country = StringField('country', [validators.required()])
    telephone = StringField('telephone', [validators.required()])


# symptom logging form
class QueryForm(FlaskForm):
    # p_id = StringField('patient_id', [validators.required()])
    
    # get patient ID and name list
    conn = sqlite3.connect('i257symtrack.db')
    c = conn.cursor()
    p_list = []
    query = """SELECT patient_id, name FROM patient"""
    for db_row in c.execute(query):
        row_pid = db_row[0]
        row_pname = str(row_pid) + ' - ' + db_row[1]
        p_list.append((row_pid,row_pname))
    conn.close()
    
    p_id = SelectField('patient_id', choices=p_list, coerce=int, option_widget=None)
    start_date = DateField('start_date', [validators.required()], format='%Y-%m-%d')
    end_date = DateField('end_date', [validators.required()], format='%Y-%m-%d')
    query_type = RadioField('Report type', [validators.required()],
                                                 choices=[  ('q1', 'Total average severity score'),
                                                            ('q2', 'Contribution of symptoms in total score'),
                                                            ('q3', 'Average severity of each symptom'),
                                                            ('q4', 'Day-wise symptom severity'),
                                                            ('q5', 'Total symptom score (date-wise)')])


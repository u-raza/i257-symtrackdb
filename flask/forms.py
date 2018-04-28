
# from flask.ext.wtf import Form // this is deprecated
from flask_wtf import Form
from wtforms import StringField, IntegerField, PasswordField, SelectField, DateField, RadioField
# from flask_wtf.html5 import EmailField // this is deprecated
from wtforms.fields.html5 import EmailField
from wtforms import validators

# patient sign up form
class PatientForm(Form):
    name = StringField('name', [validators.required()])
    dob = StringField('dob', [validators.required()])
    street_address = StringField('street_address', [validators.required()])
    city = StringField('city', [validators.required()])
    state = StringField('state', [validators.required()])
    country = StringField('country', [validators.required()])
    telephone = StringField('telephone', [validators.required()])


# symptom logging form
class QueryForm(Form):
    pid = StringField('patient_id', [validators.required()])
    start_date = DateField('start_date', [validators.required()], format='%m/%d/%Y')
    end_date = DateField('end_date', [validators.required()], format='%m/%d/%Y')
    query_type = RadioField('Report type', [validators.required()],
                                                 choices=[  ('q1', 'Average symptom score'),
                                                            ('q2', 'Contribution of symptoms in total score'),
                                                            ('q3', 'Average severity of each symptom'),
                                                            ('q4', 'Day-wise symptom severity'),
                                                            ('q4', 'Total symptom score (date-wise)')])


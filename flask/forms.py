
# from flask.ext.wtf import Form // this is deprecated
from flask_wtf import Form
from wtforms import StringField, IntegerField, PasswordField, SelectField
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
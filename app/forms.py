from wtforms import StringField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email, InputRequired, Length
from flask_wtf import FlaskForm
import re

def valid_email(form, field):
	regex = r"^[a-z0-9-_]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
	if not (re.search(field.data, regex)):
		raise ValidationError('Please provide proper email address.') 

class ContactForm(FlaskForm):
    f_name = StringField('First Name', [InputRequired(message="Please provide your First name.")])
    l_name = StringField('Last Name', [InputRequired(message="Please provide your First name.")])
    email = EmailField('Email', [InputRequired()])
    subject = StringField('Subject', [InputRequired(), Length(max="128", min="1", message="1 to 256 characters are required in this field.")])
    message = StringField('Message', [InputRequired(), Length(min="16", message="16 characters or more are required in this field.")])
    submit = SubmitField('Send')



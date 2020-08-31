from wtforms import StringField, SubmitField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email, InputRequired, Length
from wtforms.widgets import TextArea
from flask_wtf import FlaskForm
import re


class ContactForm(FlaskForm):
    f_name = StringField('First Name', [InputRequired(message="Please provide your First name.")])
    l_name = StringField('Last Name', [InputRequired(message="Please provide your First name.")])
    email = EmailField('Email', [InputRequired()])
    subject = StringField('Subject', [InputRequired(), Length(max="128", min="1", message="1 to 256 characters are required in this field.")])
    message = TextAreaField('Message', [InputRequired(), Length(min="16", message="16 characters or more are required in this field.")])
    submit = SubmitField('Send')



from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, validators

class ContactForm(Form):
    name = StringField('Name:', [validators.DataRequired()])
    email = StringField('Email:', [validators.DataRequired(), validators.Email('your@email.com')])
    message = TextAreaField('Message:', [validators.DataRequired()])
    submit = SubmitField('Submit')
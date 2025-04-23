from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField


class TaskForm(FlaskForm):
    title = StringField('Title')
    description = StringField('Description')
    submit = SubmitField('Submit')
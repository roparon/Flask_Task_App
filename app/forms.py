from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField


class TaskForm(FlaskForm):
    title = StringField('Title')
    description = TextAreaField('Description')
    completed = BooleanField('Completed')
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField

class TaskForm(FlaskForm):
   title = StringField('Task Title')
   description = TextAreaField('Task Description')
   completed = BooleanField('Completed')
   submit = SubmitField('Submit')
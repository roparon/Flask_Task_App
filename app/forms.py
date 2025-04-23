from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField

class TaskForm(FlaskForm):
   title = StringField('Task Title')
   description = TextAreaField('Task Description')
   completed = BooleanField('Completed')
   submit = SubmitField('Submit')

class UserForm(FlaskForm):
   user_name = StringField('User Name')
   first_name = StringField('First Name')
   last_name = StringField('Last Name')
   submit = SubmitField('Submit')
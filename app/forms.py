from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField,PasswordField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
   title = StringField('Task Title')
   description = TextAreaField('Task Description')
   completed = BooleanField('Completed')
   submit = SubmitField('Submit')

class UserForm(FlaskForm):
   user_name = StringField('User_Name', validators=[DataRequired()])
   first_name = StringField('First_Name', validators=[DataRequired()])
   last_name = StringField('Last_Name', validators=[DataRequired()])
   password = PasswordField('Password', validators=[DataRequired()])
   submit = SubmitField('Register')
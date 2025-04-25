from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField,PasswordField
from wtforms.validators import DataRequired
from wtforms import form

class UserForm(FlaskForm):
   user_name = StringField('User Name', validators=[DataRequired()])
   first_name = StringField('First Name', validators=[DataRequired()])
   last_name = StringField('Last Name', validators=[DataRequired()])
   password = PasswordField('Password', validators=[DataRequired()])
   submit = SubmitField('Register')
   
class TaskForm(FlaskForm):
   title = StringField('Task Title')
   description = TextAreaField('Task Description')
   completed = BooleanField('Completed')
   submit = SubmitField('Submit')

class LoginForm(FlaskForm):
   username = StringField('Username', validators=[DataRequired()])
   password = PasswordField('Password', validators=[DataRequired()])
   submit = SubmitField('Login')
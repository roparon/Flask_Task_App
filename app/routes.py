from flask import render_template
from app import app
from app.models import User
from app.forms import TaskForm
from app.forms import UserForm

@app.route('/')
def home():
    return render_template('index.html', title='Home Page')

@app.route('/tasks')
def tasks():
    form = TaskForm()
    if form.validate_on_submit():
        new_user = User(
            user_name=form.user_name.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            password=form.password.data
        )
    return render_template('tasks.html', title='Tasks', task_form=form)


@app.route('/register', methods=['POST'])
def register():
    form = UserForm()
    return render_template('register.html', users=User.query.all(), title='Users', user_form=form)
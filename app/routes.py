from flask import render_template
from app import app
from app.models import User
from app.forms import TaskForm

@app.route('/')
def home():
    return render_template('index.html', title='Home Page')

@app.route('/tasks')
def tasks():
    form = TaskForm()
    return render_template('tasks.html', title='Tasks', task_form=form)


@app.route('/users', methods=['GET', 'POST'])
def users():
    return render_template('users.html', users=User.query.all(), title='Users')
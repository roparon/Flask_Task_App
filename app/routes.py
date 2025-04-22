from flask import render_template
from app import app
from app.models import User

@app.route('/')
def home():
    return render_template('index.html', users=User.query.all(), title='Home Page')

@app.route('/tasks')
def tasks():
    return render_template('tasks.html', title='Tasks')


@app.route('/users')
def users():
    return render_template('users.html', users=User.query.all(), title='Users')
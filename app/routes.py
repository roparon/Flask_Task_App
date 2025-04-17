from flask import render_template
from app import app

users = ["rope", "jane", "john", "doe", "alice", "bob", "charlie", "dave", "eve", "frank"]
tasks = ["wash the car", "clean the house", "buy groceries", "finish homework", "call mom", "read a book", "exercise", "cook dinner", "write a report", "plan a trip"]
@app.route('/')
def home():
    return render_template('index.html', r=users)

@app.route('/tasks')
def tasks():
    return render_template('tasks.html', tasks=tasks)
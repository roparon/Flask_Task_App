from flask import render_template
from app import app

users = ["rope", "jane", "john", "doe", "alice", "bob", "charlie", "dave", "eve", "frank"]
@app.route('/')
def home():
    return render_template('index.html')
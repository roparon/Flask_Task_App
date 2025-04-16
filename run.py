from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome to Flask Task App!</h1>'
@app.route('/tasks')
def tasks():
    return 'This is your tasks list page!'
@app.route('/about')
def about():
    return '''<h1>About Us!</h1>
    <p>Hey there! 👋 This is a little project I built using Flask — a lightweight, super cool Python web framework. It’s my way of learning web development step by step, one line of code at a time.
Whether you’re a beginner like me or just curious about Flask, you’re totally welcome here! Let’s grow, code, and explore this exciting world of web apps together. 🚀

Thanks for stopping by — and keep learning! 😊</p>'''



if __name__ == '__main__':
    app.run(debug=True)
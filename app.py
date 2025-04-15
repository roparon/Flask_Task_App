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
    <p>This is my first flask-app page. Come on! let's learn new things together!😊</p>'''



if __name__ == '__main__':
    app.run(debug=True)
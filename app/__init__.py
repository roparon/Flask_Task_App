from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY']='17573a504ee98db2449daeb7662af9c44ca49f26dd6255498550c69fadfe2be6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'










from app import routes
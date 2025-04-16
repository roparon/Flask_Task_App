from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY']='17573a504ee98db2449daeb7662af9c44ca49f26dd6255498550c69fadfe2be6'










from app import routes
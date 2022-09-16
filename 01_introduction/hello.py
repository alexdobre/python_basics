from flask import Flask

app = Flask(__name__)


@app.route('/me')
def hello():
    return 'Hello, Alex!'


@app.route('/class')
def clazz():
    return 'Hello, Class!'


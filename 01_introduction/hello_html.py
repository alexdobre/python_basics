from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    name = 'Alex'
    return render_template('person_list.html', name=name)

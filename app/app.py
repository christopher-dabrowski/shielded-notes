"""Entry point of the application"""

from flask import Flask, request, render_template, current_app, session
from flask_session import Session
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

Session(app)


@app.route('/')
def index():
    # print(app.config)
    # print(current_app.config)
    session['test'] = 'TEST!'
    session['logged'] = True
    session['user_name'] = 'Tomas'
    return render_template('index.html')


@app.route('/session')
def get_session():
    print(list(str(zip(session.keys(), session.values()))))
    return str(list(zip(session.keys(), session.values())))

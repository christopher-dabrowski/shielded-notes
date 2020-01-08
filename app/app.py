"""Entry point of the application"""

from flask import Flask, request, render_template, current_app, session
from flask_session import Session
from config import Config
from account_routes import users

app = Flask(__name__)
app.config.from_object(Config)
Session(app)

app.register_blueprint(users)


@app.route('/')
def index():
    session['test'] = 'TEST!'
    session['logged'] = True
    session['user_name'] = 'Tomas'
    return render_template('index.html')


@app.route('/session')
def get_session():
    print(list(str(zip(session.keys(), session.values()))))
    return str(list(zip(session.keys(), session.values())))

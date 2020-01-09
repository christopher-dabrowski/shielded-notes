"""Entry point of the application"""

from flask import Flask, request, render_template, current_app, session
from flask_session import Session
from config import Config
from models import db, User, fill_db_with_values
from login import login_manager
from account_routes import users

app = Flask(__name__)
app.config.from_object(Config)
Session(app)

db.init_app(app)
with app.app_context():
    db.drop_all()
    db.create_all()
    fill_db_with_values()
login_manager.init_app(app)

app.register_blueprint(users)


@app.route('/')
def index():
    # FIXME: Remove this

    # session['test'] = 'TEST!'
    # session['logged'] = True
    # session['user_name'] = 'Tomas'
    return render_template('index.html')


@app.route('/session')
def get_session():
    # TODO: Remove session route
    print(list(str(zip(session.keys(), session.values()))))
    return str(list(zip(session.keys(), session.values())))

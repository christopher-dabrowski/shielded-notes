"""Entry point of the application"""

from flask import Flask, request, render_template, current_app, session
from flask_session import Session
from config import Config
from models import db, User
from account_routes import users

app = Flask(__name__)
app.config.from_object(Config)
Session(app)

db.init_app(app)
with app.app_context():
    db.drop_all()
    db.create_all()

app.register_blueprint(users)


@app.route('/')
def index():
    # FIXME: Remove this
    # db.create_all()
    # u = User(username='john', email='john@example.com')
    # db.session.add(u)
    # db.session.commit()

    # session['test'] = 'TEST!'
    # session['logged'] = True
    # session['user_name'] = 'Tomas'
    return render_template('index.html')


@app.route('/session')
def get_session():
    print(list(str(zip(session.keys(), session.values()))))
    return str(list(zip(session.keys(), session.values())))

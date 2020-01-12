"""Entry point of the application"""

from flask import Flask, request, render_template, current_app, session, redirect, url_for
from flaskext.markdown import Markdown
from flask_session import Session
from flask_login import current_user
from config import Config
from models import db, User, fill_db_with_values
from login import login_manager
from account_routes import users
from notes_routes import notes

app = Flask(__name__)
app.config.from_object(Config)
Session(app)
Markdown(app)

db.init_app(app)
with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.commit()
    fill_db_with_values()
login_manager.init_app(app)

app.register_blueprint(users)
app.register_blueprint(notes)


@app.route('/')
def index():
    return render_template('index.html')

from flask_sqlalchemy import SQLAlchemy
from flask import current_app
import bcrypt

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(), index=True, unique=True)
    email = db.Column(db.String(), index=True, unique=True)
    password_hash = db.Column(db.String())
    lucky_number = db.Column(db.Integer)

    def __repr__(self):
        return f'{self.login}'


def fill_db_with_values():
    password_hash = bcrypt.hashpw(
        'Pa$$word'.encode(), bcrypt.gensalt()).decode()

    sample_user = User(login='Tomasz', password_hash=password_hash,
                       email='tomasz@pw.edu.pl', lucky_number=17)
    db.session.add(sample_user)
    db.session.commit()

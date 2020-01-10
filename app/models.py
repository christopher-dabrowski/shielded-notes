from flask_sqlalchemy import SQLAlchemy
from flask import current_app
from flask_login import UserMixin
import bcrypt

db = SQLAlchemy()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(), index=True, unique=True)
    email = db.Column(db.String(), index=True, unique=True)
    password_hash = db.Column(db.String())
    lucky_number = db.Column(db.Integer)
    notes = db.relationship('Note', backref='owner', lazy=True)

    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(
            password.encode(), bcrypt.gensalt()).decode()

    def __repr__(self):
        return f'{self.login}'


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    heading = db.Column(db.String())
    body = db.Column(db.String())
    public = db.Column(db.Boolean())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


def fill_db_with_values():
    tomas = User(
        login='Tomasz', email='tomasz@pw.edu.pl', lucky_number=17)
    tomas.set_password('Pa$$word')
    db.session.add(tomas)

    note = Note(title='Barista potrzebny', heading='Praca',
                body='W najbliższą sobotę będzie za duży ruch w kawiarni. Potrzebny barista na jeden dzień. Dobra stawka gwarantowana.',
                owner=tomas, public=False)
    db.session.add(note)

    note = Note(title='Wszyscy mile widziani', heading='Zaproszenie',
                body='Już niedługo odbędzie się ślub mojej córki. Wszyscy goście są mile widziani. Im nas więcej tym weselej.',
                owner=tomas, public=True)
    db.session.add(note)

    db.session.commit()

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
    share_list = db.relationship('Share', backref='note', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Note id={self.id} title={self.title}>'


class Share(db.Model):
    """Many to many relation - note share list"""

    id = db.Column(db.Integer, primary_key=True)
    note_id = db.Column(db.Integer, db.ForeignKey('note.id'))
    user_name = db.Column(db.String())

    def __repr__(self):
        return f'User: {self.user_name} NoteId: {self.note_id}'


def fill_db_with_values():
    tomas = User(
        login='Tomasz', email='tomasz@pw.edu.pl', lucky_number=17)
    tomas.set_password('Pa$$word')
    db.session.add(tomas)

    note = Note(title='Barista potrzebny', heading='Praca',
                body='W najbliższą sobotę będzie za duży ruch w kawiarni. Potrzebny barista na jeden dzień. Dobra stawka gwarantowana.',
                owner=tomas, public=False)
    db.session.add(note)
    share = Share(note=note, user_name='JohnyGuitar')
    db.session.add(share)

    note = Note(title='Wszyscy mile widziani', heading='Zaproszenie',
                body='Już niedługo odbędzie się ślub mojej córki. Wszyscy goście są mile widziani. Im nas więcej tym weselej.',
                owner=tomas, public=True)
    db.session.add(note)

    johny = User(
        login='JohnyGuitar', email='jony@place.pl', lucky_number=10)
    johny.set_password('Pa$$word')
    db.session.add(johny)

    db.session.commit()

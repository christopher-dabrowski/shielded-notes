from flask_sqlalchemy import SQLAlchemy
from flask import current_app
from flask_login import UserMixin
import bcrypt

print('Starting db module')
db = SQLAlchemy()
print(db)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(), index=True, unique=True)
    email = db.Column(db.String(), index=True, unique=True)
    password_hash = db.Column(db.String())
    lucky_number = db.Column(db.Integer)

    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(
            password.encode(), bcrypt.gensalt()).decode()

    def __repr__(self):
        return f'{self.login}'


def fill_db_with_values():
    sample_user = User(
        login='Tomasz', email='tomasz@pw.edu.pl', lucky_number=17)
    sample_user.set_password('Pa$$word')

    db.session.add(sample_user)
    db.session.commit()

    sample_user.login = 'Marian'
    print('While initiating', db)
    print(db.session.dirty)
    db.session.rollback()

from flask_wtf.form import FlaskForm
from flask import current_app
from wtforms import StringField, PasswordField, ValidationError, FileField, Form, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo, NumberRange
from wtforms.csrf.session import SessionCSRF
from datetime import timedelta
from config import Config
from models import User
import bcrypt


class BaseForm(FlaskForm):
    class Meta:
        csrf = True
        csrf_class = SessionCSRF
        csrf_secret = Config.SECRET_KEY.encode()
        csrf_time_limit = timedelta(minutes=20)


class UniqueLogin(object):
    def __init__(self, message=None):
        if not message:
            message = 'Wybrany login jest zajęty'
        self.message = message

    def __call__(self, form, field):
        login = field.data
        with current_app.app_context():
            result = User.query.filter(User.login == login).first()
            if result is not None:
                raise ValidationError(self.message)


class UniqueEmail(object):
    def __init__(self, message=None):
        if not message:
            message = 'Wybrany email jest zajęty'
        self.message = message

    def __call__(self, form, field):
        email = field.data
        with current_app.app_context():
            result = User.query.filter(User.email == email).first()
            if result is not None:
                raise ValidationError(self.message)


class RegisterForm(BaseForm):
    login = StringField('login', validators=[
        DataRequired('Brak loginu'),
        Length(min=4, message='Login musi mieć co najmniej 4 znaki'),
        UniqueLogin()
    ])

    password = PasswordField('password', validators=[
        DataRequired('Brak hasła'),
        Length(min=6, message='Hasło musi mieć co najmniej 6 znaków'),
        Length(max=72, message='Hasło może mieć co najwyżej 72 znaki')
    ])
    password2 = PasswordField('Password', validators=[
        EqualTo('password', 'Hasła się różnią')
    ])

    email = StringField('Mail', validators=[
        DataRequired('Brak maila'),
        Email('Nieprawidłowy mail'),
        UniqueEmail()
    ])

    lucky_number = IntegerField('Lucky number', validators=[
        DataRequired('Brak szczęśliwej liczby :('),
        NumberRange(-10000000, 10000000,
                    'Liczba musi być z przedziału od -10000000 do 10000000')
    ])


class LoginInDatabase(object):
    def __init__(self, message=None):
        if not message:
            message = 'Podany login nie istnieje'
        self.message = message

    def __call__(self, form, field):
        login = field.data
        with current_app.app_context():
            result = User.query.filter(User.login == login).first()
            if result is None:
                raise ValidationError(self.message)


class CorrectPassword(object):
    def __init__(self, message=None):
        if not message:
            message = 'Błędne hasło'
        self.message = message

    def __call__(self, form, field):
        login = form.login.data
        password = field.data
        with current_app.app_context():
            user = User.query.filter(User.login == login).first()
            if user is None:
                return
            if not bcrypt.checkpw(password.encode(), user.password_hash.encode()):
                raise ValidationError(self.message)


class LoginForm(BaseForm):
    login = StringField('login', validators=[
        DataRequired('Brak loginu'),
        LoginInDatabase()
    ])
    password = StringField('password', validators=[
        DataRequired('Brak hasła'),
        CorrectPassword()
    ])


class ChangePasswordForm(BaseForm):
    login = StringField('login')

    old_password = PasswordField('Old password', validators=[
        DataRequired('Brak starego hasła'),
        CorrectPassword()
    ])

    password = PasswordField('password', validators=[
        DataRequired('Brak hasła'),
        Length(min=6, message='Hasło musi mieć co najmniej 6 znaków'),
        Length(max=72, message='Hasło może mieć co najwyżej 72 znaki')
    ])
    password2 = PasswordField('password2', validators=[
        EqualTo('password', 'Hasła się różnią')
    ])


class CreateNoteForm(BaseForm):
    heading = StringField(validators=[
        Length(max=15, message='Nagłówek może mieć najwyżej 15 znaków')
    ])

    title = StringField(validators=[
        DataRequired('Tytuł jest wymagany'),
        Length(max=10, message='Tytuł może mieć najwyżej 10 znaków')
    ])

    body = TextAreaField()

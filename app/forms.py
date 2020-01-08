from flask_wtf.form import FlaskForm
from wtforms import StringField, PasswordField, ValidationError, FileField, Form, IntegerField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from wtforms.csrf.session import SessionCSRF
from datetime import timedelta
from config import Config


class BaseForm(FlaskForm):
    class Meta:
        csrf = True
        csrf_class = SessionCSRF
        csrf_secret = Config.SECRET_KEY.encode()
        csrf_time_limit = timedelta(minutes=20)


class RegisterForm(BaseForm):
    login = StringField('login', validators=[
        DataRequired('Brak loginu'),
        # TODO: Check if login is free
        Length(min=4, message='Login musi mieć co najmniej 4 znaki')
    ])

    password = PasswordField('password', validators=[
        DataRequired('Brak hasła'),
        Length(min=6, message='Hasło musi mieć co najmniej 6 znaków')
    ])
    password2 = PasswordField('Password', validators=[
        # TODO: Check if mail is free
        EqualTo('password', 'Hasła się różnią')
    ])

    email = StringField('Mail', validators=[
        DataRequired('Brak maila'),
        Email('Nieprawidłowy mail')
    ])

    lucky_number = IntegerField('Lucky number', validators=[
        DataRequired('Brak szczęśliwej liczby :(')
    ])

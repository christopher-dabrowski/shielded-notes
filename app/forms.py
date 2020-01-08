from wtforms import StringField, PasswordField, ValidationError, FileField, Form
from wtforms.validators import DataRequired, Email
from wtforms.csrf.session import SessionCSRF
from datetime import timedelta
from flask import current_app


class BaseForm(Form):
    class Meta:
        csrf = True
        csrf_class = SessionCSRF
        csrf_secret = current_app.config.SECRET_KEY.encode()
        csrf_time_limit = timedelta(minutes=20)


class RegisterForm(BaseForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

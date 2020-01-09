"""Routes connected to users accounts"""

from flask import Blueprint, render_template, flash, redirect, url_for, request, session
from forms import RegisterForm, LoginForm
from models import db, User
import bcrypt

users = Blueprint('account', __name__, template_folder='templates')


@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(meta={'csrf_context': session})
    if form.validate_on_submit():
        flash('Konto zostało utworzone', 'alert-success')

        login = form.login.data
        password = form.password.data
        email = form.email.data
        lucky_number = form.lucky_number.data

        password_hash = bcrypt.hashpw(
            password.encode(), bcrypt.gensalt()).decode()

        user = User(login=login, password_hash=password_hash,
                    email=email, lucky_number=lucky_number)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))

    print('Form invalid')
    print(form.login.errors)

    users = User.query.all()
    print('Users')
    print(users)
    return render_template('register.html', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(meta={'csrf_context': session})
    if form.validate_on_submit():
        return 'Super'

    return render_template('login.html', form=form)

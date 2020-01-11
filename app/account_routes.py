"""Routes connected to users accounts"""

from flask import Blueprint, render_template, flash, redirect, url_for, request, session, current_app
from flask_login import current_user, login_user, logout_user, login_required
from forms import RegisterForm, LoginForm, ChangePasswordForm
from models import User, db, Login
import bcrypt

users = Blueprint('account', __name__, template_folder='templates')


@users.route('/register', methods=['GET', 'POST'])
def register():
    logout_user()

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

    return render_template('register.html', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    print(Login.query.all())

    form = LoginForm(meta={'csrf_context': session})
    user = User.query.filter_by(login=form.login.data).first()
    if user:  # A login attempt
        ip = request.remote_addr
        login = Login(successful=form.validate(), ip=ip, user=user)
        db.session.add(login)
        db.session.commit()

    if form.validate_on_submit():
        login_user(user)

        next_page = session.get('next', None)
        session['next'] = None
        if not next_page:
            next_page = url_for('index')
        return redirect(next_page)

    return render_template('login.html', form=form)


@users.route('/logout')
def logout():
    logout_user()
    flash('Nastąpiło poprawne wylogowanie', 'alert-success')

    return redirect(url_for('index'))


@users.route('/account')
@login_required
def account():
    return render_template('account.html')


@login_required
@users.route('/account/changePassword', methods=['GET', 'POST'])
def change_password():
    form = ChangePasswordForm(meta={'csrf_context': session})
    if form.validate_on_submit():
        password = form.password.data
        current_id = current_user.id
        user = User.query.filter_by(id=current_id).first()
        user.set_password(password)
        db.session.commit()

        flash('Hasło zostało zmienione', 'alert-success')
        return redirect(url_for('account.account'))

    return render_template('change_password.html', form=form)

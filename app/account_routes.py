"""Routes connected to users accounts"""

from flask import Blueprint, render_template, flash, redirect, url_for, request, session
from forms import RegisterForm

users = Blueprint('account', __name__, template_folder='templates')


@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(meta={'csrf_context': session})
    if form.validate_on_submit():
        flash('Konto zostało utworzone', 'alert-success')
        # TODO: Create user account
        redirect(url_for('index'))

    print('Form invalid')
    print(form.login.errors)
    print(form)
    print(form.login.errors)
    return render_template('register.html', form=form)

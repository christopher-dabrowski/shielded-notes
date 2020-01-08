"""Routes connected to users accounts"""

from flask import Blueprint

users = Blueprint('account', __name__, template_folder='templates')


@users.route('/register')
def register():
    return 'Register here'

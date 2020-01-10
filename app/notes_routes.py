"""Routes connected to user notes"""

from flask import Blueprint, render_template, redirect, flash, url_for, request
from flask_login import current_user, login_required

notes = Blueprint('notes', __name__, template_folder='templates')


@notes.route('/myNotes', methods=['GET', 'POST'])
@login_required
def my_notes():
    return render_template('my_notes.html')

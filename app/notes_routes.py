"""Routes connected to user notes"""

from flask import Blueprint, render_template, redirect, flash, url_for, request, session
from flask_login import current_user, login_required
from forms import CreateNoteForm
from models import db, User, Note

notes = Blueprint('notes', __name__, template_folder='templates')


@notes.route('/myNotes', methods=['GET', 'POST'])
@login_required
def my_notes():
    form = CreateNoteForm(meta={'csrf_context': session})
    if form.validate_on_submit():
        user = User.query.filter_by(id=current_user.id).first()

        heading = form.heading.data
        title = form.title.data
        body = form.body.data
        note = Note(title=title, heading=heading, body=body, owner=user)
        db.session.add(note)
        db.session.commit()

        print(user.notes)

    return render_template('my_notes.html', form=form)

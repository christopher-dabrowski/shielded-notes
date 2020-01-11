"""Routes connected to user notes"""

from flask import Blueprint, render_template, redirect, flash, url_for, request, session, Response, abort
from flask_login import current_user, login_required
from forms import CreateNoteForm
from models import db, User, Note, Share

notes = Blueprint('notes', __name__, template_folder='templates')


@notes.route('/myNotes', methods=['GET', 'POST'])
@login_required
def my_notes():
    user = User.query.filter_by(id=current_user.id).first()

    form = CreateNoteForm(meta={'csrf_context': session})
    if form.validate_on_submit():
        heading = form.heading.data
        title = form.title.data
        body = form.body.data
        public = form.public.data
        note = Note(title=title, heading=heading,
                    body=body, owner=user, public=public)
        db.session.add(note)

        shares_list = {row.strip() for row in form.shares.data.split()}
        for user_name in shares_list:
            share = Share(note=note, user_name=user_name)
            db.session.add(share)

        db.session.commit()

        flash('Notatka została dodana', 'alert alert-success')

    notes = user.notes
    print(notes)
    return render_template('my_notes.html', form=form, notes=notes)


@notes.route('/myNotes/delete/<int:id>')
@login_required
def delete_note(id):
    user = User.query.filter_by(id=current_user.id).first()
    notes = [note for note in user.notes if note.id == id]
    if len(notes) > 1:
        abort(500)
    if len(notes) < 1:
        abort(404)

    note = notes[0]
    db.session.delete(note)
    db.session.commit()

    return redirect(url_for('notes.my_notes'))


@notes.route('/notes')
@login_required
def view_notes():
    user = User.query.filter_by(id=current_user.id).first()

    public_notes = Note.query.filter_by(public=True).all()
    shared_with_me_id = [share.note_id for share in Share.query.filter_by(
        user_name=user.login).all()]
    notes_shared_with_me = Note.query.filter(
        Note.id.in_(shared_with_me_id)).all()

    notes = public_notes + notes_shared_with_me

    print(public_notes)
    print(notes_shared_with_me)
    print(notes)
    return render_template('view_notes.html', notes=notes)

from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from ..models import User
from . import login
from .. import db
from .forms import loginForm, RegForm

@login.route('/login', methods=('GET','POST'))
def signin():
    form = loginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.main'))
        flash('Invalid username or password')
    return render_template('login/login.html', form=form)
	
@login.route('/register', methods=['GET','POST'])
def signup():
    form = RegForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, firstname=form.firstname.data, lastname=form.lastname.data, password=form.password.data, role_id='1')
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login.signin'))
    else:
        print(form.errors)
    return render_template('login/register.html', form=form)

@login.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.main'))

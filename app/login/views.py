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
        print('on submit event')
        print(form.email.data)
    else:
        print(form.errors)
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

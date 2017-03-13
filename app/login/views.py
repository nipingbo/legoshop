from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from ..models import User
from . import login
from .forms import loginForm

@login.route('/login', methods=['GET','POST'])
def signin():
    form = loginForm()
    print("in the signin process function")

    return render_template('login/login.html', form = form)


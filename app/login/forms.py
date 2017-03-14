from app import db
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from werkzeug.security import check_password_hash
from app.models import User

#login form
class loginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password')
    remember_me = BooleanField('Remember Me', default=False)
    submit = SubmitField('Log In')

#Register form
class RegForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm_password', message='Two password must be the same')])
    firstname = StringField('Firstname', validators=[DataRequired()])
    lastname = StringField('Lastname', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])

#validate
def loginCheck(form, field):
    saved_password = db.session.query(User.password).filter(User.email == field.data).first()
    hash_password = saved_password[0]
    if saved_password is None:
        raise ValidationError('Email or Password is not correct!')

def emailCheck(form, field):
    email = db.session.query(User).filter(User.email == form.email.data).first()
    if email is not None:
        raise ValidationError('Email already exists, try to change another')

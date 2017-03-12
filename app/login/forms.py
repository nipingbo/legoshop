from app import db
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField
from wtfroms.validators import InputRequired, Length, Email, EqualTo, ValidationError
from werkzeug.security import check_password_hash
from app.models import User

#login form
class loginForm(Form):
	email = StringField('Email', validators=[InputRequired()])
	password = PasswordField('Password', validators=[InputRequired()])
	remember_me = BooleanField('Remember Me', default=False)

#Register form
class RegForm(Form):
	email = StringField('Email', validators=[InputRequired()])
	password = PasswordField('Password', validators=[InputRequired(), EqualTo('confirm_password', message='Two password must be the same')])
	confirm_password = PasswordField('Confirm Password', validators=[InputRequired()])

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
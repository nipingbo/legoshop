from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db
class User(UserMixin, db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True)
	firstname = db.Column(db.String(20), unique=False)
	lastname = db.Column(db.String(20), unique=False)
	role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
	email = db.Column(db.String(256), unique=True, index=True)
	password_hash = db.Column(db.String(128))

	@property
	def password(self):
		raise AttributeError('password is not a readable attribute')
	
	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

	def __repr__(self):
                return '<User %r>' % self.email

class Role(db.Model):
	__tablename__ = 'role'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique = True)
	users = db.relationship('User', backref='role', lazy='dynamic')
	
	def __repr__(self):
		return '<Role %r>' % self.name

class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key = True)
    productId = db.Column(db.String(16), unique = True)
    description = db.Column(db.String(256))
    release_year = db.Column(db.String(4))
    price = db.Column(db.Numeric(10,2))
    currency = db.Column(db.String(3))

    def __repr__(self):
        return '<Product %r>' % self.productId

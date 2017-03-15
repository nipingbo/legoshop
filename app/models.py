from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db, login_manager
from sqlalchemy.exc import IntegrityError
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
    productId = db.Column(db.String(16), unique = False)
    description = db.Column(db.String(256))
    release_year = db.Column(db.String(4))
    price = db.Column(db.Numeric(10,2))
    currency = db.Column(db.String(3))
    
    @staticmethod
    def generate_fake(count=100):
        import forgery_py
        import random
        from decimal import Decimal
        random.seed()
        for i in range(count):
                year = forgery_py.date.year()
                product = Product(productId=forgery_py.basic.number(10000, 75999), \
                          description = forgery_py.lorem_ipsum.words(10), \
                          release_year = year, \
                          price = Decimal(random.uniform(10,200)).quantize(Decimal('0.00')), \
                          currency = 'USD')
                print(product.productId)
                print(product.description)
                print(product.release_year)
                print(product.price)
                print(product.currency)
                db.session.add(product)
                try:
                        db.session.commit()
                except IntegrityError:
                        db.session.rollback()


    def __repr__(self):
        return '<Product %r>' % self.productId

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

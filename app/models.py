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
    product_id = db.Column(db.String(16), unique = False)
    product_name = db.Column(db.String(64))
    description = db.Column(db.String(256))
    product_category_id = db.Column(db.Integer, db.ForeignKey('product_category.id'))
    release_year = db.Column(db.String(4))
    pieces = db.Column(db.Integer)
    packaging = db.Column(db.String(1))
    status = db.Column(db.String(1))
    first_sold_date = db.Column(db.Date)
    first_sold_place = db.Column(db.String(3))
    instruction = db.Column(db.Boolean)
    price1 = db.Column(db.Numeric(10,2))
    currency1 = db.Column(db.String(3))
    price2 = db.Column(db.Numeric(10,2))
    currency2 = db.Column(db.String(3))
    price3 = db.Column(db.Numeric(10,2))
    currency3 = db.Column(db.String(3))
    settype = db.Column(db.String(1))
    @staticmethod
    def generate_fake(count=100):
        import forgery_py
        import random
        from decimal import Decimal
        random.seed()
        for i in range(count):
                year = forgery_py.date.year()
                price = Decimal(random.uniform(10,200)).quantize(Decimal('0.00'))
                product = Product(product_id=forgery_py.basic.number(10000, 75999), \
                                  product_name = forgery_py.lorem_ipsum.word(), \
                                  description = forgery_py.lorem_ipsum.words(10), \
                                  product_category_id = 1, \
                                  release_year = year, \
                                  pieces = 1000, \
                                  packaging = 'B', \
                                  status = 'A', \
                                  first_sold_date = forgery_py.date.date(), \
                                  first_sold_place = 'USA', \
                                  instruction = True, \
                                  price1 = price, \
                                  currency1 = 'USD', \
                                  price2 = price / Decimal('1.12'), \
                                  currency2 = 'EUR', \
                                  settype = 'N')
                db.session.add(product)
                try:
                        db.session.commit()
                except IntegrityError:
                        db.session.rollback()


    def __repr__(self):
        return '<Product %r>' % self.productId

class Product_Category(db.Model):
	__tablename__ = 'product_category'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique = True)
	products = db.relationship('Product', backref='product_category', lazy='dynamic')
	
	def __repr__(self):
		return '<Product Category %r>' % self.name

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

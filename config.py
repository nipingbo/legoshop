import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'legoshop'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True;
	MAIL_SUBJECT_PREFIX = '[Legoshop]'
	MAIL_SENDER = 'Legoshop Admin <knight_ni@163.com>'
	FLASK_ADMIN = os.environ.get('FLASK_ADMIN')

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True
	MAIL_SERVER = 'smtp.163.com'
	MAIL_PORT = 465
	MAIL_USE_TLS = False
	MAIL_USE_SSL = True
	MAIL_USER = 'knight_ni@613.com'
	MAIL_PASSWORD = 'Happygame99'
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Happy9@localhost:3306/legoshop'

class TestingConfig(Config):
	Testing = True
	MAIL_SERVER = 'MAIL.21CN.COM'
	MAIL_PORT = 587
	MAIL_USER = ''
	MAIL_PASSWORD = ''
	SQLALCHEMY_DATABASE_URI = ''

class ProductConfig(Config):
	Testing = True
	MAIL_SERVER = 'MAIL.21CN.COM'
	MAIL_PORT = 587
	MAIL_USER = ''
	MAIL_PASSWORD = ''
	SQLALCHEMY_DATABASE_URI = ''

config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'product': ProductConfig,
	'default': DevelopmentConfig
	}
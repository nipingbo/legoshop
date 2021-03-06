from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config

bootstrap = Bootstrap()
mail = Mail()
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection='strong'
login_manager.login_view = 'login.signin'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .login import login as login_blueprint
    app.register_blueprint(login_blueprint)

    from .productmgr import prdmgr as product_blueprint
    app.register_blueprint(product_blueprint)
    return app

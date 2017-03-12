from flask import render_template, session, redirect, url_for, current_app
from .. import db
from .. models import Product
from . import main as main_blueprint

@main_blueprint.route('/', methods=['GET', 'POST'])
def main():
    products = Product.query.all()
    return render_template('main/index.html', products=products)
@main_blueprint.route('/about')
def about():
    return render_template('about/About.html')


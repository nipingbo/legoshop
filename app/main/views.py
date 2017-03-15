from flask import render_template, session, redirect, url_for, current_app,request
from .. import db
from .. models import Product
from . import main as main_blueprint

@main_blueprint.route('/', methods=['GET', 'POST'])
def main():
    page = request.args.get('page', 1, type=int)
    pagination = Product.query.paginate(page, per_page=5, error_out = False)
    products = pagination.items
    return render_template('main/index.html', products=products, pagination=pagination )
@main_blueprint.route('/about')
def about():
    return render_template('about/About.html')


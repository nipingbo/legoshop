from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from .. models import Product, Product_Category
from . import prdmgr
from .. import db
from .forms import productForm

@prdmgr.route('/products', methods=['GET','POST'])
@login_required
def maintain_products():
    form = productForm()

    return render_template('productmgr/products.html', form = form)

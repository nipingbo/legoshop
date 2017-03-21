from flask import Blueprint
prdmgr = Blueprint('prdmgr', __name__)
from . import views

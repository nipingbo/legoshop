from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateField, DecimalField, TextAreaField, IntegerField, \
        SelectField
from wtforms.validators import DataRequired, Length, ValidationError,NumberRange
from app.models import Product

class productForm(FlaskForm):
    product_id = StringField('Lego ID', validators=[DataRequired(), Length(max=8)])
    product_name = StringField('Lego Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Length(max=256)])
    product_category = StringField('Lego Category')
    release_year = StringField('Release Year', validators=[Length(4)])
    pieces = IntegerField('Pieces', validators=[NumberRange(min=10,max=99999)])
    packaging = StringField('Packaging')
    status = SelectField('Current Status', choices=[('A','For Sale'),('R','Retired')])
    first_sold_date = DateField('First Sold Date', format='%Y%m%d', render_kw={'class':'form-control datepicker'})
    first_sold_place = StringField('First Sold Place', validators=[Length(3)])
    instruction = BooleanField('Has Instruction')
    price1 = DecimalField('First Sales Price')
    currency1 = StringField('Currency')


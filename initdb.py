import os
from app import create_app, db, models
app = create_app('default')
#Use db.create_all without the app_context will be failure
with app.app_context():
    db.drop_all()
    db.create_all()

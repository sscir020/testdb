from app import create_app,db
from app.models import *

app=create_app('development')
app.app_context().push()
with  app.app_context():
    db.drop_all()
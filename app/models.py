from .__init__ import db

class Item(db.Model):
    __tablename__='items'
    item_id=db.Column(db.Integer,nullable=False,primary_key=True)
    item_name=db.Column(db.String(32),nullable=False,unique=True,index=True)
    num=db.Column(db.Integer,nullable=False,default=0)
    comment=db.Column(db.String(20),nullable=True,default='')

class Users(db.Model):
    __bind_key__ = 'users'
    user_id = db.Column(db.Integer, nullable=False, primary_key=True)
    user_name = db.Column(db.String(64), nullable=False, unique=True, index=True)
    user_pass =db.Column(db.String(64), nullable=False)
    role = db.Column(db.Integer, nullable=False, default=1)
from flask import session,render_template
from . import ctr
from ..models import Item
# from ..models1 import Item
from .. import db
# from ..__init__ import DBSession
@ctr.route('/')#,methods=['GET','POST']
@ctr.route('/index')
def index():
    return render_template('index.html')

@ctr.route('/show_add_item_act',methods=['GET',''])
def show_add_item():
    return render_template('add.html')


@ctr.route('/show_items_act',methods=['GET',''])
def show_items():
    # db.session.commit()
    items=Item.query.all()
    # db.session.flush()
    db.session.close()
    print("*********************")
    # session=DBSession()
    # items=session.query(Item).all()

    return render_template('show.html',items=items)
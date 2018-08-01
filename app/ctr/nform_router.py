from flask import session,render_template
from . import ctr
from ..models import Item
# from ..models1 import Item
from .. import db
# from ..__init__ import DBSession
# from ..__init__ import dbsession
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
    # items=Item.query.all()
    # db.session.flush()
    print("*********************")
    # session=DBSession()
    # items=dbsession.query(Item).all()
    items=Item.query.all()

    return render_template('show.html',items=items)
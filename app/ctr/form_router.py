from flask import request,redirect,url_for
from . import ctr
from ..models import Item
from ..__init__ import db

@ctr.route('/add_item_act',methods=['','POST'])
def add_item():
    item_id=request.form['input_number_id']
    item_num=request.form['input_number_num']
    i=Item.query.filter_by(item_id=item_id).first()
    i.num+=int(item_num)
    db.session.add(i)
    db.session.commit()
    return redirect(url_for('ctr.show_items'))


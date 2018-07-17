from flask import request,redirect,url_for
from . import ctr
from ..models import Item
from ..__init__ import db
import threading
lock=threading.Lock()

@ctr.route('/add_new_item_act',methods=['','POST'])
def add_new_item():
    item_name=request.form['input_text_name']
    item_num=request.form['input_number_num']
    if item_name!='' and item_num!='':
        lock.acquire()
        i=Item(item_name=item_name,num=item_num)
        db.session.add(i)
        db.session.flush()
        db.session.commit()
        db.session.close()
        lock.release()
    return redirect(url_for('ctr.show_items'))

@ctr.route('/add_item_act',methods=['','POST'])
def add_item():
    item_id=request.form['input_number_id']
    item_num=request.form['input_number_num']
    if item_id!='' and item_num!='':
        lock.acquire()
        i=Item.query.filter_by(item_id=item_id).first()
        if i!=None:
            i.num+=int(item_num)
            db.session.add(i)
            db.session.flush()
            db.session.commit()
            db.session.close()
        lock.release()
    return redirect(url_for('ctr.show_items'))


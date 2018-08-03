from flask import request,redirect,url_for,render_template
from . import ctr
from ..models import Item,Users
from ..__init__ import db
from .form import ChangeItemForm,ChangePassForm,ChangeItemAForm

# from ..models1 import Item
# from ..__init__ import dbsession
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
        db.session.commit()
        db.session.flush()
        db.session.close()

        # dbsession.add(i)
        # dbsession.commit()
        # dbsession.close()
        lock.release()
    return redirect(url_for('ctr.show_items'))

@ctr.route('/change_item_act',methods=['','POST'])
def change_item():
    item_id=request.form['input_number_id']
    item_num=request.form['input_number_num']
    if item_id!='' and item_num!='':
        lock.acquire()
        i=Item.query.filter_by(item_id=item_id).first()
        if i!=None:
            i.num+=int(item_num)
            db.session.add(i)
            db.session.commit()
            db.session.flush()
            db.session.refresh(i)
        db.session.close()
        print("---------------")
        # i = dbsession.query(Item).filter(Item.item_id==item_id).one()
        # if i!=None:
        #     i.num+=int(item_num)
        #     dbsession.add(i)
        #     dbsession.commit()
        #     dbsession.close()
        lock.release()
    return redirect(url_for('ctr.show_items'))



@ctr.route('/form_change_item_act',methods=['GET','POST'])
def form_change_item():
    form=ChangeItemForm()
    # items =None
    print(form.data)
    print(request.form)
    if form.validate_on_submit():
        i=Item.query.filter_by(item_id=form.id.data).first()
        if i!=None:
            i.num+=int(form.num.data)
            db.session.add(i)
            db.session.commit()
            db.session.flush()
            # db.session.refresh(i)
        db.session.close()
        print("---------------")
    items = Item.query.all()
    # db.session.flush()
    db.session.close()
    print("*********************")
    return render_template('show_item.html',form=form,items=items)

@ctr.route('/form_change_pass_act',methods=['GET','POST'])
def form_change_pass():
    form=ChangePassForm()
    # items =None
    if form.validate_on_submit():
        u=Users.query.filter_by(user_name=form.username.data).first()
        if u!=None:
            u.user_pass=int(form.password.data)
            db.session.add(u)
            db.session.commit()
            db.session.flush()
            # db.session.refresh(i)
        db.session.close()
        print("---------------")
    users = Users.query.all()
    # db.session.flush()
    db.session.close()
    print("*********************")
    return render_template('show_user.html',form=form,users=users)


@ctr.route('/form_change_comment_act',methods=['GET','POST'])
def form_change_comment():
    print("---------------")
    form=ChangeItemForm()
    # items =None
    print(form)
    print(form.data)
    print(request.form)
    print(form.validate())
    if request.method=='POST':
        i=Item.query.filter_by(item_id=form.id.data).first()
        if i!=None:
            i.num+=int(form.num.data)
            db.session.add(i)
            db.session.commit()
            db.session.flush()
            # db.session.refresh(i)
        db.session.close()
        print("---------------")
    items = Item.query.all()
    # db.session.flush()
    db.session.close()
    print("*********************")
    print("*********************")
    return render_template('show_itemA.html',form=form,items=items)

@ctr.route('/form_change_commentA_act',methods=['GET','POST'])
def form_change_commentA():
    print("---------------")
    form=ChangeItemAForm(request.form)
    # items =None
    print(form)
    print(form.data)
    print(request.form)
    print(form.validate())
    if request.method=='POST':
        # i=Item.query.filter_by(item_id=form.id.data).first()
        i=db.session.query(Item).filter_by(item_id=form.id.data).first()
        sql=db.session.query(Item).filter_by(item_id=form.id.data)
        print(sql)
        print(i)
        if i!=None:
            i.num+=int(form.num.data)
            db.session.add(i)
            db.session.commit()
            db.session.flush()
            # db.session.refresh(i)
        db.session.close()
        print("---------------")
    items = db.session.query(Item).all()
    # db.session.flush()
    db.session.close()
    print("*********************")
    print("***--------------****")
    return render_template('show_itemA.html',form=form,items=items)
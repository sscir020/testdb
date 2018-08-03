from flask_wtf import FlaskForm
from wtforms import IntegerField,SubmitField,StringField,SelectField,Form,RadioField,BooleanField
from wtforms.validators import DataRequired
from main_config import type

class ChangeItemForm(FlaskForm):
    id=IntegerField("id",validators=[DataRequired()],default=4)
    num=IntegerField("num",validators=[DataRequired()],default=2)
    num1=IntegerField("num")
    select = SelectField("操作", choices=[(1, '入库'), (2, '取消购买')])
    submit=SubmitField("submit")

class ChangeItemAForm(Form):
    id=IntegerField("id",validators=[DataRequired()],default=4)
    num=IntegerField("num",validators=[DataRequired()],default=2)
    radio=RadioField("num",choices=[(type.apple, '入库'), (type.orange, '取消购买')],validators=[DataRequired()])
    bool=BooleanField("num",default='unchecked')
    select = SelectField("操作", choices=[(type.apple, '入库'), (type.orange, '取消购买')],validators=[DataRequired()])
    submit=SubmitField("submit")

class ChangePassForm(FlaskForm):
    username=StringField("username",validators=[DataRequired()])
    password=StringField("password")
    submit=SubmitField("submit")
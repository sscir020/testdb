from flask_wtf import FlaskForm
from wtforms import IntegerField,SubmitField,StringField
from wtforms.validators import DataRequired


class ChangeItemForm(FlaskForm):
    id=IntegerField("id",validators=[DataRequired()],default=4)
    num=IntegerField("num",validators=[DataRequired()],default=2)
    submit=SubmitField("submit")

class ChangePassForm(FlaskForm):
    username=StringField("username",validators=[DataRequired()])
    password=StringField("password")
    submit=SubmitField("submit")
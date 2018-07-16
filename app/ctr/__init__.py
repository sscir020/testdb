#coding:utf-8
from flask import Blueprint

ctr=Blueprint('ctr',__name__)

from . import nform_router,form_router

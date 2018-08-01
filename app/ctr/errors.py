#coding:utf-8
from . import ctr
from ..__init__ import db
# from ..__init__ import dbsession

@ctr.app_errorhandler(404)
def page_not_found(e):
    # dbsession.close()
    # dbsession.rollback()
    db.session.close()
    db.session.rollback()
    return "not found 404"

@ctr.app_errorhandler(500)
def internal_error(e):
    # dbsession.close()
    # dbsession.close()
    db.session.rollback()
    db.session.rollback()
    return "internal 500"

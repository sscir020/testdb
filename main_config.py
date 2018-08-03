#coding:utf-8
import os
from enum import Enum
basedir = os.path.abspath(os.path.dirname(__file__))
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

class Config:
    SECRET_KEY =  '1AR4bnTnLHZyHaKt' #os.environ.get('SECRET_KEY') or
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:hard_guess@localhost:3306/testing?charset=utf8'
    SQLALCHEMY_BINDS ={
        'users':'mysql+pymysql://root:hard_guess@localhost:3306/testdb1?charset=utf8',
    }
    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_MAX_OVERFLOW = 0
    # SQLALCHEMY_ISOLATION_LEVEL= 'SERIALIZABLE'
    # SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    FLASK_NUM_PER_PAGE = 5
    FLASK_NUM_PER_PAGE_LIST = 6
#SESSION_TYPE= 'redis'
    # SESSION_PERMANENT = False
    # SESSION_KEY_PREFIX='sessionprefix'
    MAX_CHAR_PER_COMMENT = 20

    @staticmethod
    def init_app(app):
        pass

#
# class DevelopmentConfig(Config):
#     DEBUG = True
#     SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:hard_guess@localhost:3306/testing?charset=utf8'
#
#
# class Development2Config(Config):
#     DEBUG = True
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///D:\\projects\\testdb\\database\\data.sqlite'
#
# class TestingConfig(Config):
#     TESTING = True
#     SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Aosien2016@120.76.207.142:3306/inventory?charset=utf8'
#
# config = {
#     'development': DevelopmentConfig,
#     'development2': Development2Config,
#     'testing': TestingConfig,
#     'default': DevelopmentConfig
# }

class type(Enum):
    apple=1
    orange=2
    lemon=3

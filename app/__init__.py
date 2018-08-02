from flask import Flask,session
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from main_config import Config#config

# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import create_engine

db=SQLAlchemy()
bootstrap=Bootstrap()

# engine=create_engine( 'mysql+pymysql://root:hard_guess@localhost:3306/testing?charset=utf8')
# DBSession=sessionmaker(bind=engine)
# dbsession=DBSession()
def create_app(config_name):
    app = Flask(__name__)
    # app.config.from_object(config[config_name])
    # config[config_name].init_app(app)
    app.config.from_object(Config)
    Config.init_app(app)

    db.init_app(app)
    bootstrap.init_app(app)

    from app.ctr import ctr
    app.register_blueprint(ctr)


    return app
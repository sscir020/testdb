from flask import Flask,session
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from main_config import config


db=SQLAlchemy()
bootstrap=Bootstrap()



def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    bootstrap.init_app(app)

    from app.ctr import ctr
    app.register_blueprint(ctr)


    return app
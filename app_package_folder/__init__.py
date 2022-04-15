from flask import Flask
from app_package_folder.Config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


db = SQLAlchemy()
ma = Marshmallow()

def create_app(config_class_test=Config):
    app = Flask(__name__)
    app.config.from_object(config_class_test)
    
    
    #location of database
    basedir = os.path.abspath(os.path.dirname(__file__))

    # Database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'db.sqlite')
    # not necessary but TravisMedia says it will complain in console if we don't do this
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Init db
    # db = SQLAlchemy(app)
    db.init_app(app)
    #Init ma
    # ma = Marshmallow(app)
    ma.init_app(app)
    
    
    
    from app_package_folder.app import api_route
    # from app_package_folder.errors_handling import bp
    
    app.register_blueprint(api_route)
    # app.register_blueprint(bp)
    
    return app
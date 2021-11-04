from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow



# Allows python to communicate to database 
db= SQLAlchemy()
ma = Marshmallow()

def create_app ():

    # Creates a Flask App
    app = Flask (__name__)

    app.config.from_object("config.app_config")

    db.init_app(app)
    ma.init_app(app)
    
    with app.app_context():
        db.create_all()

    from controllers import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint(controller)
  

    return app
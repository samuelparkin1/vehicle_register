import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Allows python to communicate to database 
db= SQLAlchemy()

def create_app ():

    # Creates a Flask App
    app = Flask (__name__)

    app.config.from_object("config.app_config")

    db.init_app(app)

    from controllers import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint(controller)
  

    return app
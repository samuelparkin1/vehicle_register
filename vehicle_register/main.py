from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_login import LoginManager
from marshmallow.exceptions import ValidationError



# Allows python to communicate to database 
db= SQLAlchemy()
ma = Marshmallow()
lm = LoginManager()


def create_app ():

    # Creates a Flask App
    app = Flask (__name__)

    app.config.from_object("config.app_config")

    db.init_app(app)
    ma.init_app(app)
    lm.init_app(app)

    from commands import db_commands
    app.register_blueprint(db_commands)    
    
    from controllers import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint(controller)
 
    @app.errorhandler(ValidationError)
    def handle_bad_request(error):
        return (jsonify(error.messages), 400)
    return app
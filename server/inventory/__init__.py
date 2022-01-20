from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager

from .config import DevelopmentConfig, TestingConfig, ProductionConfig


db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()


def create_app(config="production"):
    app = Flask(__name__)

    if config == "production":
        app.config.from_object(ProductionConfig)
    elif config == "testing":
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        from .models import User, List, Item, Category

        db.create_all()

    from inventory.handlers import (
        auth_handler,
        users_handler,
        lists_handler,
        category_handler,
    )

    app.register_blueprint(auth_handler)
    app.register_blueprint(users_handler)
    app.register_blueprint(lists_handler)
    app.register_blueprint(category_handler)

    # Generic error handler for all routes
    @app.errorhandler(HTTPException)
    def handle_exception(e: HTTPException):
        """Return JSON instead of HTML for HTTP errors."""

        response = e.get_response()
        http_code = e.code or 500

        response.data = {
            "code": http_code,
            "name": e.name,
            "description": e.description,
        }

        return jsonify(response), http_code

    return app

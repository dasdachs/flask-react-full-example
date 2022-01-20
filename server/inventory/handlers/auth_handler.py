from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

from inventory import db
from inventory.models import User


auth_handler = Blueprint("auth_handler", __name__, url_prefix="/api/v1/auth")


@auth_handler.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        # Note: this is not proper validation
        return {"msg": "Provide a username and password"}, 422

    user = User(username=username)
    user.hash_password(password)

    db.session.add(user)
    db.session.commit()

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)


@auth_handler.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    print(data)

    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()

    if not user or not user.compare_password(password):
        return {"msg": "Invalid username or password"}, 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

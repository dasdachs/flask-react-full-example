from flask import Blueprint, jsonify, abort, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from inventory import db
from inventory.models import User
from inventory.seralizers import user_schema, users_schema


users_handler = Blueprint("users_handler", __name__, url_prefix="/api/v1/users")


@users_handler.route("")
@jwt_required()
def get_users():
    try:
        users = User.query.all()

        return jsonify(users_schema.dump(users))
    except:
        abort(500)


@users_handler.route("/<int:user_id>", methods=["GET", "PATCH", "DELETE"])
@jwt_required()
def get_update_delete_user(user_id: int):
    user = User.query.filter_by(id=user_id).first()

    if not user:
        abort(404)

    current_user = get_jwt_identity()

    if current_user != user.username:
        abort(403, f"You do not have permission to access this users data")

    if request.method == "DELETE":
        db.session.delete(user)
        db.session.commit()

        return {}, 204

    if request.method == "PATCH":
        username = request.get_json().get("username")

        user.username = username

        db.session.add(user)
        db.session.commit()

        return jsonify(user_schema.dump(user)), 201

    return jsonify(user_schema.dump(user))

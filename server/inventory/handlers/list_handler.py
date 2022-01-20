import json

from flask import Blueprint, jsonify, abort, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.sql import or_

from inventory import db
from inventory.models import User, List
from inventory.models.items import Item
from inventory.seralizers import list_schema, lists_schema, items_schema, item_schema


lists_handler = Blueprint("list_handler", __name__, url_prefix="/api/v1/lists")


@lists_handler.route("/public")
def public_list():
    try:
        lists = List.query.filter_by(is_public=True).all()

        return jsonify(lists_schema.dump(lists))
    except:
        abort(500)

@lists_handler.route("", methods=["GET", "POST"])
@jwt_required()
def get_lists():
    current_user = get_jwt_identity()
    user = User.query.filter_by(username=current_user).first()

    if not user:
        abort(403)
    if request.method == "POST":
    
        data = request.get_json()

        list_item = list_schema.load(data, session=db.session)
        list_item.user_id = user.id

        db.session.add(list_item)
        db.session.commit()

        return jsonify(list_schema.dump(list_item)), 201
    else:
        try:
            lists = List.query.filter(or_(user_id=user.id, is_public=True)).all()

            return jsonify(lists_schema.dump(lists))
        except:
            abort(500)


@lists_handler.route("/<int:list_id>", methods=["GET", "PATCH", "DELETE"])
@jwt_required()
def get_update_delete_list(list_id: int):
    list: List = List.query.filter_by(id=list_id).first()

    if not list:
        abort(404)

    current_user = get_jwt_identity()

    if current_user != list.user.username:
        abort(403, description=f"You do not have permission to access this item")

    if request.method == "DELETE":
        db.session.delete(list)
        db.session.commit()

        return {}, 204

    if request.method == "PATCH":
        data = request.get_json()

        list_item = list_schema.load(data, session=db.session)
        list.name = list_item.name
        list.is_public = list_item.is_public

        db.session.add(list)
        db.session.commit()

        return jsonify(list_schema.dump(list)), 201

    return jsonify(list_schema.dump(list))


@lists_handler.route("/<int:list_id>/items", methods=["GET", "POST"])
@jwt_required()
def get_or_add_items(list_id: int):
    list: List = List.query.filter_by(id=list_id).first()

    if not list:
        abort(404)

    current_user = get_jwt_identity()

    if current_user != list.user.username:
        abort(403, description=f"You do not have permission to access this item")

    if request.method == "POST":
        data = request.get_json()

        item = item_schema.load(data, session=db.session)
        item.list_id = list_id

        db.session.add(item)
        db.session.commit()

        return jsonify(item_schema.dump(item)), 201

    items = Item.query.filter_by(list_id=list_id).all()

    return jsonify(items_schema.dump(items))

from flask import Blueprint, jsonify, abort, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from inventory import db
from inventory.models import Category
from inventory.seralizers import categories_schema, category_schema


category_handler = Blueprint(
    "category_handler", __name__, url_prefix="/api/v1/categories"
)


@category_handler.route("", methods=["GET", "POST"])
@jwt_required()
def get_categories():
    if request.method == "POST":
        category = category_schema.load(request.get_json(), session=db.session)

        db.session.add(category)
        db.session.commit()

        return jsonify(category_schema.dump(category)), 201
    else:
        try:
            categories = Category.query.all()

            return jsonify(categories_schema.dump(categories))
        except:
            abort(500)


@category_handler.route("/<int:category_id>", methods=["GET", "PATCH", "DELETE"])
@jwt_required()
def get_update_delete_category(category_id: int):
    category = Category.query.filter_by(id=category_id).first()

    if not category:
        abort(404)

    if request.method == "DELETE":
        db.session.delete(category)
        db.session.commit()

        return {}, 204

    if request.method == "PATCH":
        new_name = request.get_json().get("name")

        if new_name:
            category.name = new_name
            db.session.add(category)
            db.session.commit()

        return jsonify(category_schema.dump(category)), 201

    return jsonify(category_schema.dump(category))

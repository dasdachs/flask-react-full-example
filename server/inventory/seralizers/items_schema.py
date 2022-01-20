from marshmallow_sqlalchemy.fields import Nested

from inventory import ma
from inventory.models import Category, Item


class ItemSchema(ma.SQLAlchemySchema):
    class Meta:
        load_instance = True
        model = Item

    id = ma.auto_field()
    name = ma.auto_field()
    quantity = ma.auto_field()
    min_quantity = ma.auto_field()
    category_id = ma.auto_field()
    category = ma.auto_field(dump_only=True)


class CategorySchema(ma.SQLAlchemySchema):
    class Meta:
        load_instance = True
        model = Category

    name = ma.auto_field()
    items = Nested(ItemSchema, many=True, exclude=("category", "category_id"))


category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)

item_schema = ItemSchema()
items_schema = ItemSchema(many=True)

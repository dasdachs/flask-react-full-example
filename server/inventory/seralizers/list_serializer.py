from inventory import ma
from inventory.models import List


class ListSchema(ma.SQLAlchemySchema):
    class Meta:
        load_instance = True
        model = List

    id = ma.auto_field()
    name = ma.auto_field()
    is_public = ma.auto_field()
    user = ma.auto_field()
    # items = ma.auto_field()


class ListsSchema(ma.SQLAlchemySchema):
    class Meta:
        model = List

    id = ma.auto_field()
    name = ma.auto_field()
    is_public = ma.auto_field()
    user = ma.auto_field()


list_schema = ListSchema()
lists_schema = ListsSchema(many=True)

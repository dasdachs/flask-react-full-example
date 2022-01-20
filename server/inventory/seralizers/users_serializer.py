from inventory import ma
from inventory.models import User


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        load_instance = True
        model = User

    id = ma.auto_field()
    username = ma.auto_field()


user_schema = UserSchema()
users_schema = UserSchema(many=True)

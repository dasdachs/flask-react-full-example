"""Serializers help us convert python classes into JSON objects

For example this will not work:

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))

...

from .models import User

@app.route("/users")
def get_users():
    users = User.query.all()
    
    return users
    
As Flask has no idea how to represent you class as a object. 

We could of course sent the dict version of the class, e.g. user.__dict__
but that might not be ideal, as we want to keep some fields to ourself, like
the password.

So we would need to add a `serialize` method to each class. And that would work, 
but we would soon see that is repetitive and that we want more and more features.

This is where Marshmallow comes in. Marshmalling is the process of converting objects
into JSON and Flask-Marshmallow is by far the easiest approach for us to do it.
"""
from .items_schema import item_schema, categories_schema, category_schema, items_schema
from .list_serializer import list_schema, lists_schema
from .users_serializer import user_schema, users_schema


__all__ = [
    "categories_schema",
    "category_schema",
    "item_schema",
    "items_schema",
    "list_schema",
    "lists_schema",
    "user_schema",
    "users_schema",
]

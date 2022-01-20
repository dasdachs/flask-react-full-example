from inventory import db


class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    quantity = db.Column(db.Integer(), nullable=False)
    min_quantity = db.Column(db.Integer(), nullable=False)

    # Items have categories so we add the category_id
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)
    # ... and create a "virtual" property category on this class and
    # "items" on the Category item
    category = db.relationship("Category", backref=db.backref("items", lazy="dynamic"))

    # Same as above for lists with the addition that `lazy` is False that's because
    # we need all the items on the list when we get retrive it
    list_id = db.Column(db.Integer, db.ForeignKey("lists.id"), nullable=False)
    list = db.relationship("List", backref=db.backref("items", lazy="dynamic"))

    def __repr__(self) -> str:
        return f"<Item name={self.name} quantity={self.quantity}>"


class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Category name={self.name}>"

from db import db

class ProductsCategoriesXref(db.Model):
    __tablename__ = 'productscategoriesxref'
    
    product_id = db.Column(db.String, db.ForeignKey('products.product_id'), primary_key=True)
    category_id = db.Column(db.String, db.ForeignKey('categories.category_id'), primary_key=True)

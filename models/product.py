from db import db
import uuid

class Product(db.Model):
    __tablename__ = 'products'
    
    product_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    company_id = db.Column(db.String, db.ForeignKey('companies.company_id'), nullable=False)
    company_name = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String)
    active = db.Column(db.Boolean, default=True)
    
    warranty = db.relationship('Warranty', backref='product', lazy=True)
    categories = db.relationship('ProductsCategoriesXref', backref='product', lazy=True)

from flask_sqlalchemy import SQLAlchemy
import uuid

db = SQLAlchemy()

class Company(db.Model):
    __tablename__ = 'companies'
    company_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    company_name = db.Column(db.String, unique=True, nullable=False)

    def as_dict(self):
        return {"company_id": self.company_id, "company_name": self.company_name}

class Category(db.Model):
    __tablename__ = 'categories'
    category_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    category_name = db.Column(db.String, unique=True, nullable=False)

    def as_dict(self):
        return {"category_id": self.category_id, "category_name": self.category_name}

class Product(db.Model):
    __tablename__ = 'products'
    product_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    company_id = db.Column(db.String, db.ForeignKey('companies.company_id'), nullable=False)
    company_name = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String)
    active = db.Column(db.Boolean, default=True)

    def as_dict(self):
        return {
            "product_id": self.product_id,
            "company_id": self.company_id,
            "company_name": self.company_name,
            "price": self.price,
            "description": self.description,
            "active": self.active
        }

class Warranty(db.Model):
    __tablename__ = 'warranties'
    warranty_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    product_id = db.Column(db.String, db.ForeignKey('products.product_id'), nullable=False)
    warranty_months = db.Column(db.String, nullable=False)

    def as_dict(self):
        return {"warranty_id": self.warranty_id, "product_id": self.product_id, "warranty_months": self.warranty_months}

class ProductCategoryXref(db.Model):
    __tablename__ = 'productscategoriesxref'
    product_id = db.Column(db.String, db.ForeignKey('products.product_id'), primary_key=True)
    category_id = db.Column(db.String, db.ForeignKey('categories.category_id'), primary_key=True)

    def as_dict(self):
        return {"product_id": self.product_id, "category_id": self.category_id}

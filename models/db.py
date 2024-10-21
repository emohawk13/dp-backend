from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/dbname'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()

class Company(db.Model):
    company_id = db.Column(db.String, primary_key=True)
    company_name = db.Column(db.String, unique=True, nullable=False)
    products = db.relationship('Product', backref='company', lazy=True)

class Product(db.Model):
    product_id = db.Column(db.String, primary_key=True)
    company_id = db.Column(db.String, db.ForeignKey('company.company_id'), nullable=False)
    company_name = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String)
    active = db.Column(db.Boolean, default=True)

class Category(db.Model):
    category_id = db.Column(db.String, primary_key=True)
    category_name = db.Column(db.String, unique=True, nullable=False)

class Warranty(db.Model):
    warranty_id = db.Column(db.String, primary_key=True)
    product_id = db.Column(db.String, db.ForeignKey('product.product_id'), nullable=False)
    warranty_months = db.Column(db.String, nullable=False)

class ProductsCategoriesXref(db.Model):
    product_id = db.Column(db.String, db.ForeignKey('product.product_id'), primary_key=True)
    category_id = db.Column(db.String, db.ForeignKey('category.category_id'), primary_key=True)

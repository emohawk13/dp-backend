import uuid
import os
from flask import Flask
from models import db, Company, Category, Product, Warranty, ProductCategoryXref
from sqlalchemy.exc import SQLAlchemyError

def create_test_data(app):
    with app.app_context():
        try:
            # Create all tables
            db.create_all()
            print("All tables created successfully.")

            # Clear existing data 
            Company.query.delete()
            Category.query.delete()
            Product.query.delete()
            Warranty.query.delete()
            ProductCategoryXref.query.delete()
            db.session.commit()
            print("Existing data cleared.")

            # Create Companies
            company1 = Company(company_name="Hasbro")
            company2 = Company(company_name="Mattel")
            db.session.add_all([company1, company2])
            db.session.commit()
            print("Companies added.")

            # Create Categories
            category1 = Category(category_name="Board Games")
            category2 = Category(category_name="Action Figures")
            category3 = Category(category_name="Puzzles")
            db.session.add_all([category1, category2, category3])
            db.session.commit()
            print("Categories added.")

            # Create Products
            product1 = Product(
                company_id=company1.company_id,
                company_name=company1.company_name,
                price=19.99,
                description="Classic Monopoly Game",
                active=True
            )
            product2 = Product(
                company_id=company1.company_id,
                company_name=company1.company_name,
                price=9.95,
                description="Hasbro Gaming Clue Game",
                active=True
            )
            product3 = Product(
                company_id=company2.company_id,
                company_name=company2.company_name,
                price=14.99,
                description="Barbie Action Figure",
                active=False
            )
            db.session.add_all([product1, product2, product3])
            db.session.commit()
            print("Products added.")

            # Create Warranties
            warranty1 = Warranty(
                product_id=product1.product_id,
                warranty_months="24 months"
            )
            warranty2 = Warranty(
                product_id=product2.product_id,
                warranty_months="12 months"
            )
            db.session.add_all([warranty1, warranty2])
            db.session.commit()
            print("Warranties added.")

            # Create Product-Category Xrefs
            xref1 = ProductCategoryXref(
                product_id=product1.product_id,
                category_id=category1.category_id
            )
            xref2 = ProductCategoryXref(
                product_id=product2.product_id,
                category_id=category1.category_id
            )
            xref3 = ProductCategoryXref(
                product_id=product3.product_id,
                category_id=category2.category_id
            )
            db.session.add_all([xref1, xref2, xref3])
            db.session.commit()
            print("Product-Category relationships added.")

            print("Test data creation completed successfully.")

        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    # Get database username and password from user input
    username = input("Enter your PostgreSQL username: ")
    password = input("Enter your PostgreSQL password: ")
    db_name = input("Enter your PostgreSQL database name: ")
    host = input("Enter your PostgreSQL host (default: localhost): ") or "localhost"
    port = input("Enter your PostgreSQL port (default: 5432): ") or "5432"

    # Create the database URI dynamically
    DATABASE_URI = f'postgresql://{username}:{password}@{host}:{port}/{db_name}'

    # Set DATABASE_URI as an environment variable
    os.environ['DATABASE_URI'] = DATABASE_URI

    app = Flask(__name__)
    
    # Use the environment variable in app configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    create_test_data(app)

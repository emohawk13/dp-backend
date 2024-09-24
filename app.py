from flask import Flask, jsonify, request
from models import db, Company, Category, Product, Warranty, ProductCategoryXref
from sqlalchemy.exc import SQLAlchemyError
from create_db import create_test_data  # Import the create_test_data function

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)

# Ensure the test data is created before running the app
with app.app_context():
    # Run the database creation before starting the Flask app
    create_test_data(app)  

# CREATE Operations

@app.route('/company', methods=['POST'])
def create_company():
    try:
        data = request.get_json()
        new_company = Company(company_name=data['company_name'])
        db.session.add(new_company)
        db.session.commit()
        return jsonify({'message': 'Company created successfully'}), 201
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/categories', methods=['POST'])
def create_category():
    try:
        data = request.get_json()
        new_category = Category(category_name=data['category_name'])
        db.session.add(new_category)
        db.session.commit()
        return jsonify({'message': 'Category created successfully'}), 201
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/products', methods=['POST'])
def create_product():
    try:
        data = request.get_json()
        new_product = Product(
            company_id=data['company_id'],
            company_name=data['company_name'],
            price=data['price'],
            description=data['description'],
            active=data['active']
        )
        db.session.add(new_product)
        db.session.commit()
        return jsonify({'message': 'Product created successfully'}), 201
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/warranties', methods=['POST'])
def create_warranty():
    try:
        data = request.get_json()
        new_warranty = Warranty(
            product_id=data['product_id'],
            warranty_months=data['warranty_months']
        )
        db.session.add(new_warranty)
        db.session.commit()
        return jsonify({'message': 'Warranty created successfully'}), 201
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/products_categories', methods=['POST'])
def create_product_category_xref():
    try:
        data = request.get_json()
        new_xref = ProductCategoryXref(
            product_id=data['product_id'],
            category_id=data['category_id']
        )
        db.session.add(new_xref)
        db.session.commit()
        return jsonify({'message': 'Product-Category Xref created successfully'}), 201
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 400

# READ Operations

@app.route('/companies', methods=['GET'])
def get_companies():
    companies = Company.query.all()
    return jsonify([company.as_dict() for company in companies])

@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.as_dict() for product in products])

@app.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return jsonify([category.as_dict() for category in categories])

@app.route('/warranties', methods=['GET'])
def get_warranties():
    warranties = Warranty.query.all()
    return jsonify([warranty.as_dict() for warranty in warranties])

@app.route('/products/active', methods=['GET'])
def get_active_products():
    active_products = Product.query.filter_by(active=True).all()
    return jsonify([product.as_dict() for product in active_products])

@app.route('/products/company/<company_id>', methods=['GET'])
def get_products_by_company(company_id):
    products = Product.query.filter_by(company_id=company_id).all()
    return jsonify([product.as_dict() for product in products])

@app.route('/company/<company_id>', methods=['GET'])
def get_company_by_id(company_id):
    company = Company.query.get(company_id)
    if company:
        return jsonify(company.as_dict())
    return jsonify({'error': 'Company not found'}), 404

@app.route('/category/<category_id>', methods=['GET'])
def get_category_by_id(category_id):
    category = Category.query.get(category_id)
    if category:
        products = Product.query.join(ProductCategoryXref).filter_by(category_id=category_id).all()
        return jsonify({
            'category': category.as_dict(),
            'products': [product.as_dict() for product in products]
        })
    return jsonify({'error': 'Category not found'}), 404

@app.route('/product/<product_id>', methods=['GET'])
def get_product_by_id(product_id):
    product = Product.query.get(product_id)
    if product:
        warranty = Warranty.query.filter_by(product_id=product_id).first()
        categories = Category.query.join(ProductCategoryXref).filter_by(product_id=product_id).all()
        return jsonify({
            'product': product.as_dict(),
            'warranty': warranty.as_dict() if warranty else None,
            'categories': [category.as_dict() for category in categories]
        })
    return jsonify({'error': 'Product not found'}), 404

@app.route('/warranty/<warranty_id>', methods=['GET'])
def get_warranty_by_id(warranty_id):
    warranty = Warranty.query.get(warranty_id)
    if warranty:
        return jsonify(warranty.as_dict())
    return jsonify({'error': 'Warranty not found'}), 404

# UPDATE Operations

@app.route('/company/<company_id>', methods=['PUT'])
def update_company(company_id):
    company = Company.query.get(company_id)
    if company:
        data = request.get_json()
        company.company_name = data.get('company_name', company.company_name)
        db.session.commit()
        return jsonify({'message': 'Company updated successfully'})
    return jsonify({'error': 'Company not found'}), 404

@app.route('/category/<category_id>', methods=['PUT'])
def update_category(category_id):
    category = Category.query.get(category_id)
    if category:
        data = request.get_json()
        category.category_name = data.get('category_name', category.category_name)
        db.session.commit()
        return jsonify({'message': 'Category updated successfully'})
    return jsonify({'error': 'Category not found'}), 404

@app.route('/product/<product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get(product_id)
    if product:
        data = request.get_json()
        product.company_name = data.get('company_name', product.company_name)
        product.price = data.get('price', product.price)
        product.description = data.get('description', product.description)
        product.active = data.get('active', product.active)
        db.session.commit()
        return jsonify({'message': 'Product updated successfully'})
    return jsonify({'error': 'Product not found'}), 404

@app.route('/warranty/<warranty_id>', methods=['PUT'])
def update_warranty(warranty_id):
    warranty = Warranty.query.get(warranty_id)
    if warranty:
        data = request.get_json()
        warranty.warranty_months = data.get('warranty_months', warranty.warranty_months)
        db.session.commit()
        return jsonify({'message': 'Warranty updated successfully'})
    return jsonify({'error': 'Warranty not found'}), 404

# DELETE Operations

@app.route('/product/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product:
        Warranty.query.filter_by(product_id=product_id).delete()
        ProductCategoryXref.query.filter_by(product_id=product_id).delete()
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'Product deleted successfully'})
    return jsonify({'error': 'Product not found'}), 404

@app.route('/category/<category_id>', methods=['DELETE'])
def delete_category(category_id):
    category = Category.query.get(category_id)
    if category:
        ProductCategoryXref.query.filter_by(category_id=category_id).delete()
        db.session.delete(category)
        db.session.commit()
        return jsonify({'message': 'Category deleted successfully'})
    return jsonify({'error': 'Category not found'}), 404

@app.route('/company/<company_id>', methods=['DELETE'])
def delete_company(company_id):
    company = Company.query.get(company_id)
    if company:
        Product.query.filter_by(company_id=company_id).delete()
        db.session.delete(company)
        db.session.commit()
        return jsonify({'message': 'Company deleted successfully'})
    return jsonify({'error': 'Company not found'}), 404

@app.route('/warranty/<warranty_id>', methods=['DELETE'])
def delete_warranty(warranty_id):
    warranty = Warranty.query.get(warranty_id)
    if warranty:
        db.session.delete(warranty)
        db.session.commit()
        return jsonify({'message': 'Warranty deleted successfully'})
    return jsonify({'error': 'Warranty not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

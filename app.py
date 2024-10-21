from flask import Flask, request, jsonify
from db import init_db, db
from models.company import Company
from models.category import Category
from models.product import Product
from models.warranty import Warranty
from models.productscategoriesxref import ProductsCategoriesXref

app = Flask(__name__)
init_db(app)

@app.route('/company', methods=['POST'])
def create_company():
    data = request.get_json()
    new_company = Company(company_name=data['company_name'])
    db.session.add(new_company)
    db.session.commit()
    return jsonify({"message": "Company created", "company": data}), 201

@app.route('/companies', methods=['GET'])
def get_companies():
    companies = Company.query.all()
    result = [{"company_id": c.company_id, "company_name": c.company_name} for c in companies]
    return jsonify(result), 200

@app.route('/company/<id>', methods=['PUT'])
def update_company(id):
    data = request.get_json()
    company = Company.query.get(id)
    if company:
        company.company_name = data.get('company_name', company.company_name)
        db.session.commit()
        return jsonify({"message": "Company updated", "company": data}), 200
    return jsonify({"message": "Company not found"}), 404

@app.route('/company/delete/<id>', methods=['DELETE'])
def delete_company(id):
    company = Company.query.get(id)
    if company:
        db.session.delete(company)
        db.session.commit()
        return jsonify({"message": "Company deleted"}), 200
    return jsonify({"message": "Company not found"}), 404

@app.route('/category', methods=['POST'])
def create_category():
    data = request.get_json()
    new_category = Category(category_name=data['category_name'])
    db.session.add(new_category)
    db.session.commit()
    return jsonify({"message": "Category created", "category": data}), 201

@app.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    result = [{"category_id": c.category_id, "category_name": c.category_name} for c in categories]
    return jsonify(result), 200

@app.route('/category/delete/<id>', methods=['DELETE'])
def delete_category(id):
    category = Category.query.get(id)
    if category:
        db.session.delete(category)
        db.session.commit()
        return jsonify({"message": "Category deleted"}), 200
    return jsonify({"message": "Category not found"}), 404

@app.route('/product', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = Product(
        company_id=data['company_id'],
        company_name=data['company_name'],
        price=data['price'],
        description=data.get('description', ''),
        active=data.get('active', True)
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "Product created", "product": data}), 201

@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    result = []
    for p in products:
        warranty = Warranty.query.filter_by(product_id=p.product_id).first()
        categories = ProductsCategoriesXref.query.filter_by(product_id=p.product_id).all()
        result.append({
            "product_id": p.product_id,
            "company_name": p.company_name,
            "price": p.price,
            "description": p.description,
            "active": p.active,
            "warranty": {"warranty_months": warranty.warranty_months} if warranty else None,
            "categories": [{"category_id": c.category_id} for c in categories]
        })
    return jsonify(result), 200

@app.route('/warranty', methods=['POST'])
def create_warranty():
    data = request.get_json()
    new_warranty = Warranty(
        product_id=data['product_id'],
        warranty_months=data['warranty_months']
    )
    db.session.add(new_warranty)
    db.session.commit()
    return jsonify({"message": "Warranty created", "warranty": data}), 201

@app.route('/product/delete/<id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    if product:
        db.session.delete(product)
        Warranty.query.filter_by(product_id=id).delete()
        ProductsCategoriesXref.query.filter_by(product_id=id).delete()
        db.session.commit()
        return jsonify({"message": "Product and associated records deleted"}), 200
    return jsonify({"message": "Product not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

from flask import Blueprint, request, jsonify
from models.db import db, Product, Warranty, Category, ProductsCategoriesXref

product_bp = Blueprint('product_bp', __name__)

# CREATE a new product
@product_bp.route('/product', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = Product(
        product_id=data['product_id'], 
        company_id=data['company_id'], 
        company_name=data['company_name'], 
        price=data['price'], 
        description=data['description'], 
        active=data['active']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "Product created", "product": data}), 201

# READ all products (include warranty and associated categories)
@product_bp.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    result = []
    for p in products:
        warranty = Warranty.query.filter_by(product_id=p.product_id).first()
        categories = db.session.query(Category).join(ProductsCategoriesXref).filter(ProductsCategoriesXref.product_id == p.product_id).all()
        product_data = {
            "product_id": p.product_id,
            "company_name": p.company_name,
            "price": p.price,
            "description": p.description,
            "active": p.active,
            "warranty": {"warranty_id": warranty.warranty_id, "warranty_months": warranty.warranty_months} if warranty else None,
            "categories": [{"category_id": c.category_id, "category_name": c.category_name} for c in categories]
        }
        result.append(product_data)
    return jsonify(result), 200

# READ active products
@product_bp.route('/products/active', methods=['GET'])
def get_active_products():
    active_products = Product.query.filter_by(active=True).all()
    return jsonify([{"product_id": p.product_id, "company_name": p.company_name, "price": p.price, "description": p.description} for p in active_products]), 200

# READ a single product by ID (including associated categories)
@product_bp.route('/product/<id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    if product:
        warranty = Warranty.query.filter_by(product_id=product.product_id).first()
        categories = db.session.query(Category).join(ProductsCategoriesXref).filter(ProductsCategoriesXref.product_id == product.product_id).all()
        return jsonify({
            "product_id": product.product_id,
            "company_name": product.company_name,
            "price": product.price,
            "description": product.description,
            "active": product.active,
            "warranty": {"warranty_id": warranty.warranty_id, "warranty_months": warranty.warranty_months} if warranty else None,
            "categories": [{"category_id": c.category_id, "category_name": c.category_name} for c in categories]
        }), 200
    return jsonify({"message": "Product not found"}), 404

# UPDATE a product
@product_bp.route('/product/<id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()
    product = Product.query.get(id)
    if product:
        product.company_name = data.get('company_name', product.company_name)
        product.price = data.get('price', product.price)
        product.description = data.get('description', product.description)
        product.active = data.get('active', product.active)
        db.session.commit()
        return jsonify({"message": "Product updated", "product": data}), 200
    return jsonify({"message": "Product not found"}), 404

# DELETE a product
@product_bp.route('/product/delete/<id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    if product:
        db.session.delete(product)
        # Also delete the associated warranty and product-category links
        Warranty.query.filter_by(product_id=id).delete()
        ProductsCategoriesXref.query.filter_by(product_id=id).delete()
        db.session.commit()
        return jsonify({"message": "Product and associated records deleted"}), 200
    return jsonify({"message": "Product not found"}), 404

@product_bp.route('/product/category', methods=['POST'])
def add_product_category():
    data = request.get_json()
    new_association = ProductsCategoriesXref(product_id=data['product_id'], category_id=data['category_id'])
    db.session.add(new_association)
    db.session.commit()
    return jsonify({"message": "Product and category linked", "association": data}), 201

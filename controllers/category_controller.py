from flask import Blueprint, request, jsonify
from models.db import db, Category

category_bp = Blueprint('category_bp', __name__)

# CREATE a new category
@category_bp.route('/category', methods=['POST'])
def create_category():
    data = request.get_json()
    new_category = Category(category_id=data['category_id'], category_name=data['category_name'])
    db.session.add(new_category)
    db.session.commit()
    return jsonify({"message": "Category created", "category": data}), 201

# READ all categories
@category_bp.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return jsonify([{"category_id": c.category_id, "category_name": c.category_name} for c in categories]), 200

# READ a single category by ID
@category_bp.route('/category/<id>', methods=['GET'])
def get_category(id):
    category = Category.query.get(id)
    if category:
        return jsonify({"category_id": category.category_id, "category_name": category.category_name}), 200
    return jsonify({"message": "Category not found"}), 404

# UPDATE a category
@category_bp.route('/category/<id>', methods=['PUT'])
def update_category(id):
    data = request.get_json()
    category = Category.query.get(id)
    if category:
        category.category_name = data.get('category_name', category.category_name)
        db.session.commit()
        return jsonify({"message": "Category updated", "category": data}), 200
    return jsonify({"message": "Category not found"}), 404

# DELETE a category
@category_bp.route('/category/delete/<id>', methods=['DELETE'])
def delete_category(id):
    category = Category.query.get(id)
    if category:
        db.session.delete(category)
        db.session.commit()
        return jsonify({"message": "Category deleted"}), 200
    return jsonify({"message": "Category not found"}), 404

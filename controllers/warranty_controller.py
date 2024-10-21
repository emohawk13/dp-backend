from flask import Blueprint, request, jsonify
from models.db import db, Warranty

warranty_bp = Blueprint('warranty_bp', __name__)

# CREATE a new warranty
@warranty_bp.route('/warranty', methods=['POST'])
def create_warranty():
    data = request.get_json()
    new_warranty = Warranty(
        warranty_id=data['warranty_id'], 
        product_id=data['product_id'], 
        warranty_months=data['warranty_months']
    )
    db.session.add(new_warranty)
    db.session.commit()
    return jsonify({"message": "Warranty created", "warranty": data}), 201

# READ all warranties
@warranty_bp.route('/warranties', methods=['GET'])
def get_warranties():
    warranties = Warranty.query.all()
    return jsonify([{"warranty_id": w.warranty_id, "product_id": w.product_id, "warranty_months": w.warranty_months} for w in warranties]), 200

# READ a single warranty by ID
@warranty_bp.route('/warranty/<id>', methods=['GET'])
def get_warranty(id):
    warranty = Warranty.query.get(id)
    if warranty:
        return jsonify({
            "warranty_id": warranty.warranty_id,
            "product_id": warranty.product_id,
            "warranty_months": warranty.warranty_months
        }), 200
    return jsonify({"message": "Warranty not found"}), 404

# UPDATE a warranty
@warranty_bp.route('/warranty/<id>', methods=['PUT'])
def update_warranty(id):
    data = request.get_json()
    warranty = Warranty.query.get(id)
    if warranty:
        warranty.warranty_months = data.get('warranty_months', warranty.warranty_months)
        db.session.commit()
        return jsonify({"message": "Warranty updated", "warranty": data}), 200
    return jsonify({"message": "Warranty not found"}), 404

# DELETE a warranty
@warranty_bp.route('/warranty/delete/<id>', methods=['DELETE'])
def delete_warranty(id):
    warranty = Warranty.query.get(id)
    if warranty:
        db.session.delete(warranty)
        db.session.commit()
        return jsonify({"message": "Warranty deleted"}), 200
    return jsonify({"message": "Warranty not found"}), 404

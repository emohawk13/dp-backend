from flask import Blueprint, request, jsonify
from models.db import db, Company

company_bp = Blueprint('company_bp', __name__)

# CREATE a new company
@company_bp.route('/company', methods=['POST'])
def create_company():
    data = request.get_json()
    new_company = Company(company_id=data['company_id'], company_name=data['company_name'])
    db.session.add(new_company)
    db.session.commit()
    return jsonify({"message": "Company created", "company": data}), 201

# READ all companies
@company_bp.route('/companies', methods=['GET'])
def get_companies():
    companies = Company.query.all()
    return jsonify([{"company_id": c.company_id, "company_name": c.company_name} for c in companies]), 200

# READ a single company by ID
@company_bp.route('/company/<id>', methods=['GET'])
def get_company(id):
    company = Company.query.get(id)
    if company:
        return jsonify({"company_id": company.company_id, "company_name": company.company_name}), 200
    return jsonify({"message": "Company not found"}), 404

# UPDATE a company
@company_bp.route('/company/<id>', methods=['PUT'])
def update_company(id):
    data = request.get_json()
    company = Company.query.get(id)
    if company:
        company.company_name = data.get('company_name', company.company_name)
        db.session.commit()
        return jsonify({"message": "Company updated", "company": data}), 200
    return jsonify({"message": "Company not found"}), 404

# DELETE a company
@company_bp.route('/company/delete/<id>', methods=['DELETE'])
def delete_company(id):
    company = Company.query.get(id)
    if company:
        db.session.delete(company)
        db.session.commit()
        return jsonify({"message": "Company deleted"}), 200
    return jsonify({"message": "Company not found"}), 404


from flask import Flask, jsonify, request

app = Flask(__name__)

product_records = [
    {
        "product_id": "1",
        "product_name": "Hasbro Gaming Clue Game",
        "description": "One murder... 6 suspects...",
        "price": 9.95,
        "active": True
    },
    {
        "product_id": "2",
        "product_name": "Monopoly Board Game The Classic Edition, 2-8 players",
        "description": "Relive the Monopoly experiences...",
        "price": 35.50,
        "active": False
    }
]

# CREATE: Add a new product
@app.route('/product', methods=['POST'])
def create_product():
    new_product = request.get_json()
    product_records.append(new_product)
    return jsonify({"message": "Product added successfully", "product": new_product}), 201

# READ: Get all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(product_records), 200

# READ: Get all active products
@app.route('/product/active', methods=['GET'])
def get_active_products():
    active_products = [product for product in product_records if product.get("active")]
    return jsonify(active_products), 200

# READ: Get a product by product_id
@app.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
    product = next((product for product in product_records if product["product_id"] == product_id), None)
    if product:
        return jsonify(product), 200
    return jsonify({"error": "Product not found"}), 404

# UPDATE: Update a product by product_id
@app.route('/product/<product_id>', methods=['PUT'])
def update_product(product_id):
    updated_data = request.get_json()
    product = next((product for product in product_records if product["product_id"] == product_id), None)
    
    if product:
        product.update(updated_data)
        return jsonify({"message": "Product updated successfully", "product": product}), 200
    return jsonify({"error": "Product not found"}), 404

# UPDATE: Toggle product active status
@app.route('/product/activity/<product_id>', methods=['PUT'])
def toggle_product_activity(product_id):
    product = next((product for product in product_records if product["product_id"] == product_id), None)
    
    if product:
        product["active"] = not product["active"]
        return jsonify({"message": "Product activity toggled", "product": product}), 200
    return jsonify({"error": "Product not found"}), 404

# DELETE: Delete a product by product_id
@app.route('/product/delete', methods=['DELETE'])
def delete_product():
    product_id = request.args.get('product_id')
    product = next((product for product in product_records if product["product_id"] == product_id), None)
    
    if product:
        product_records.remove(product)
        return jsonify({"message": "Product deleted successfully"}), 200
    return jsonify({"error": "Product not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

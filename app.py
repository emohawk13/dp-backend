from flask import Flask
from models.db import init_db
from controllers.company_controller import company_bp
from controllers.category_controller import category_bp
from controllers.product_controller import product_bp
from controllers.warranty_controller import warranty_bp

app = Flask(__name__)
app.config.from_pyfile('.env')

# Initialize database
init_db(app)

# Register blueprints for each route
app.register_blueprint(company_bp)
app.register_blueprint(category_bp)
app.register_blueprint(product_bp)
app.register_blueprint(warranty_bp)

if __name__ == '__main__':
    app.run(debug=True)

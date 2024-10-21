from flask_sqlalchemy import SQLAlchemy
from config import Config 

db = SQLAlchemy()

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{Config.username}:{Config.password}@{Config.host}:{Config.port}/{Config.dbname}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()

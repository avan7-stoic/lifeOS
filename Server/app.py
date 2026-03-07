# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy


# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/lifeos'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

from flask import Flask, jsonify
from extensions import db, jwt
from models import User
from auth import auth_bp

def create_app():
    app = Flask(__name__)

    # Config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/lifeos'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # change in production

    # Init extensions
    db.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(auth_bp)


    # Health check route
    @app.route('/api/health', methods=['GET'])
    def health():
        return jsonify({"status": "ok", "message": "lifeOS backend running"})

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

from flask import Flask, jsonify
from config import Config
from extensions import db, migrate
from routes import resgister_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    #initialise database
    db.init_app(app)

    #attach migration engine to app and db
    migrate.init_app(app,db)

    # Ensure models are imported so migrations can detect them
    with app.app_context():
        import models  # noqa: F401

    #register API routes
    register_routes(app)


    @app.route('/')
    def health():
        return jsonify({"status": "ok"}), 200
    return app

if __name__ == "__main__":
    app = create_app()
    # Run on port 5555 to match the challenge instructions
    app.run(port=5555, debug=True)
from flask import Flask
from src.extensions import db, migrate
from src.routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object('src.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    register_routes(app)

    return app

app = create_app()
# FILE: src/routes/__init__.py
from flask import Blueprint

def register_routes(app):
    # Import blueprints here to avoid circular imports
    from .campers import campers_bp
    from .activities import activities_bp
    from .signups import signups_bp

    app.register_blueprint(campers_bp)
    app.register_blueprint(activities_bp)
    app.register_blueprint(signups_bp)
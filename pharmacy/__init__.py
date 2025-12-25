import os
from flask import Flask
from .extensions import db

def create_app():

    app = Flask(__name__)
    app.secret_key = "dev-secret"

    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:FerrariRoma%40V12@localhost/pharmacy_db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from .routes.medicine_routes import medicine_bp
    app.register_blueprint(medicine_bp)

    from .routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp)

    @app.before_request
    def require_login():
        from flask import request, redirect, session
        if request.endpoint not in ("auth.login", "static"):
            if "role" not in session:
                return redirect("/login")

    return app

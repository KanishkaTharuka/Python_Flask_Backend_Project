from flask import Flask
from .config import Config
from .extensions import db, jwt, mail

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)

    from .routes.user_routes import user_bp
    app.register_blueprint(user_bp)

    from .routes.otp_routes import otp_bp
    app.register_blueprint(otp_bp)

    with app.app_context():
        db.create_all()

    return app
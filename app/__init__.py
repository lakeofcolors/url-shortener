from flask import Flask

from .core.config import Base
from .core.extensions import db, migrate, ma


def create_app(config=Base):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    from .url_shortener import bp as url_shortener_bp
    app.register_blueprint(url_shortener_bp)

    return app



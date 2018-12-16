from sanic import Sanic
#  from sanic.response import json
from config import Config


def create_app(config_class=Config):
    app = Sanic(__name__)
    app.config.from_object(config_class)
    from app.api.users import bp as users_bp
    app.blueprint(users_bp, url_prefix='/users')

    return app

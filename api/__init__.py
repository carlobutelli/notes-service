#!/usr/bin/env python3
import os
import sys
import logging
import uuid

from flasgger import Swagger
from flask import Flask, request, g
from flask_cors import CORS

from api.core import get_db
from .config import DevelopmentConfig, LocalConfig, TestingConfig, ProductionConfig
from .core import Core


def create_app():
    app = Flask(__name__)

    if not os.getenv('APP_SETTINGS'):
        app_settings = f"api.config.DevelopmentConfig"
    else:
        app_settings = f"api.config.{os.getenv('APP_SETTINGS')}Config"
    app.config.from_object(app_settings)

    Core(app)
    CORS(app)

    # shell context for flask cli
    app.shell_context_processor({"app": app})

    # log handler
    log_level = logging.INFO if not app.config.get("DEBUG") else logging.DEBUG
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(log_level)
    handler.setFormatter(logging.Formatter(
        "[%(asctime)s] %(levelname)s: %(message)s "
        "[in %(pathname)s:%(lineno)d]"
    ))

    logging.getLogger("flask_cors").level = logging.DEBUG

    for h in app.logger.handlers:
        app.logger.removeHandler(h)
    app.logger.addHandler(handler)
    app.logger.setLevel(log_level)

    # registering blueprints
    app.logger.info("[WARMUP]: Registering Blueprints")
    from .admin.views import admin as admin_bp
    from .user.views import user as user_bp
    app.register_blueprint(admin_bp)
    app.register_blueprint(user_bp)

    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec_1',
                "route": '/apispec_1.json',
                "rule_filter": lambda rule: True,  # all in
                "model_filter": lambda tag: True,  # all in
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/swagger/"
    }
    Swagger(app, template_file="docs/swagger_template.json", config=swagger_config)

    app.logger.info("[WARMUP]: app successfully instantiated")

    @app.before_request
    def set_transaction_id():
        transaction_id = request.headers.get("X-Request-Id")
        g.transaction_id = transaction_id if transaction_id else str(uuid.uuid4().hex)

    return app

# __init__.py is a special Python file that allows a directory to become
# a Python package so it can be accessed using the 'import' statement.

from datetime import datetime
import os

from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_user import UserManager
from flask_wtf.csrf import CSRFProtect
from flask_socketio import SocketIO, emit

# Instantiate Flask extensions
db = SQLAlchemy()
migrate = Migrate()


def create_app(extra_config_settings={}):
    """
    Create a Flask application.
    """
    # Instantiate Flask
    app = Flask(__name__)

    # Load common settings
    app.config.from_object('app.settings')
    # Load environment specific settings
    app.config.from_object('app.local_settings')
    # Load extra settings from extra_config_settings param
    # app.config.update(extra_config_settings)

    # Setup Flask-SQLAlchemy
    db.init_app(app)

    # Setup Flask-Migrate
    migrate.init_app(app, db)

    # Register blueprints
    from .views import register_blueprints
    register_blueprints(app)

    # Setup Flask-User to handle user account related forms
    from .models.user_models import User
    from .views.main_views import user_profile_page

    # Setup Flask-User
    user_manager = UserManager(app, db, User)

    @app.context_processor
    def context_processor():
        return dict(user_manager=user_manager)

    return app

    # Log errors using: app.logger.error('Some error message')

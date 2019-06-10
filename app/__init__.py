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
from .factory import create_app, db

APP = create_app(__name__)
SOCKET_IO = SocketIO(APP)

from app.coin import websockets as coin
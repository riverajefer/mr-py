"""This file sets up a command line manager.

Use "python manage.py" for a list of available commands.
Use "python manage.py runserver" to start the development web server on localhost:5000.
Use "python manage.py runserver --help" for a list of runserver options.
"""

from flask_migrate import MigrateCommand
from flask_script import Manager
from app import create_app, SOCKET_IO
from app.commands import InitDbCommand
from app.coin.acceptors import CoinAcceptor
from app import APP, SOCKET_IO
coinAcceptor = CoinAcceptor()

MANAGER = Manager(APP)

MANAGER.add_command('db', MigrateCommand)
MANAGER.add_command('init_db', InitDbCommand)

@MANAGER.command
def runserver():
    SOCKET_IO.run(APP, host= '0.0.0.0')

if __name__ == "__main__":
    MANAGER.run()
    coinAcceptor.start

# python manage.py runserver --help     # shows available runserver options
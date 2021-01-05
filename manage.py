import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_cors import CORS

from app.main import create_app
from app import blueprint

app = create_app(os.environ.get('DEVELOPMENT_MODE') or 'dev')
app.register_blueprint(blueprint)
CORS(app)
app.app_context().push()

manager = Manager(app)

# Db initialization
# migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run()

@manager.command
def test():
    # Runs the unit test
    tests = unittest.TestLoader().discover('app/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()
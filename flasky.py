#!./venv/bin/python
import os
from app import create_app, db
from app.models import User, Role, Permission, Post
from flask_migrate import Migrate, upgrade

app = create_app('default')  # (os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role, Permission=Permission, Post=Post)


@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@app.cli.command()
def deploy():
    """Run deployment tasks."""
    upgrade()
    Role.insert_roles()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

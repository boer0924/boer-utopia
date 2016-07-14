#!venv/bin/python
from app import app, db
from utils import green_text
from migrate.versioning import api
import os.path

SQLALCHEMY_MIGRATE_REPO = app.config['SQLALCHEMY_MIGRATE_REPO']
SQLALCHEMY_DATABASE_URI = app.config['SQLALCHEMY_DATABASE_URI']
db.create_all()
if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO,
                        api.version(SQLALCHEMY_MIGRATE_REPO))
print '/'.join([basedir, database]), green_text('was created!!!')

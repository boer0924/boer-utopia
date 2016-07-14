#!/data/python/flasker/venv/bin/python
import imp
from app import app, db
from utils import green_text
from migrate.versioning import api

SQLALCHEMY_MIGRATE_REPO = app.config['SQLALCHEMY_MIGRATE_REPO']
SQLALCHEMY_DATABASE_URI = app.config['SQLALCHEMY_DATABASE_URI']

v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
migration = SQLALCHEMY_MIGRATE_REPO + '/versions/%03d_migration.py' % (v + 1)
tmp_module = imp.new_module('old_model')
# imp.new_module(name)
# Return a new empty module object called name
old_model = api.create_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
exec (old_model, tmp_module.__dict__)
script = api.make_update_script_for_model(SQLALCHEMY_DATABASE_URI,
                                          SQLALCHEMY_MIGRATE_REPO,
                                          tmp_module.meta, db.metadata)
with open(migration, 'wt') as f:
    f.write(script)
api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print green_text('New migration saved as ') + migration
print green_text('Current database version: ') + str(v)

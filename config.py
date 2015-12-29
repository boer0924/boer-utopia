import os

class BaseConfig(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = 'Microblog-Dev'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    POSTS_PER_PAGE = 9
    HOT_POSTS_COUNT = 3

class TestConfig(BaseConfig):
    DEBUG = True
    CSRF_ENABLED = True

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = 'C6\x1dO\xc9\xb1\x92Vd\xc4\xc9\xb5\xe18\x97]\x85\xe1\xa9\x100G\x9f\xbf'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    POSTS_PER_PAGE = 10
## system env
# export APP_SETTINGS="config.DevelopmentConfig"
# export DATABASE_URL="sqlite:///boer-utopia.db"
# export DATABASE_URL="postgresql://localhost/boer-utopia"

## system package
# sudo apt-get insall libffi-dev python-dev

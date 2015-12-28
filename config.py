import os

class BaseConfig(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = 'Microblog-Dev'
    # basedir = os.path.abspath(os.path.dirname(__file__))
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'boer-utopia.db')
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    POSTS_PER_PAGE = 9

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
## system env
# export APP_SETTINGS="config.DevelopmentConfig"
# export DATABASE_URL="sqlite:///boer-utopia.db"
# export DATABASE_URL="postgresql://localhost/boer-utopia"

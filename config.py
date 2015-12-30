import os

class BaseConfig(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = 'Microblog-Dev'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    POSTS_PER_PAGE = 3
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
# heroku config:set APP_SETTINGS="config.ProductionConfig" --remote heroku
# export DATABASE_URL="sqlite:///boer-utopia.db"
# export DATABASE_URL="postgresql://localhost/boer-utopia"
# heroku config:set DATABASE_URL=postgres://zhyardeyonnuqu:1lwEnSM_Zo7IH3s4WFH56d-hwm@ec2-23-21-96-129.compute-1.amazonaws.com:5432/d8q03lruh33ml0

## system package
# sudo apt-get install libffi-dev python-dev
# sudo apt-get install postgresql postgresql-server-dev-9.3

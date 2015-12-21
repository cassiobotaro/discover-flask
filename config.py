import os
# deafult config


class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '\xbf\xa9p;\xaf8~\x88\xe5\xd9\xd8\xe1JB'\
                 '\xefN\xa0\x8fn\x92n,\x8dD'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False

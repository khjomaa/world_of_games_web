import os


class Config(object):
    ENV = os.environ.get('ENV')
    CSRF_ENABLED = True
    SECRET_KEY = 'my_secret_key'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


class DevelopmentConfig(Config):
    DEBUG = True
    DB_USERNAME = os.environ.get('DB_USERNAME')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_HOST = os.environ.get('DB_HOST')
    DATABASE_NAME = os.environ.get('DATABASE_NAME')
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://%s:%s@%s:3306/%s?charset=utf8" % (DB_USERNAME, DB_PASSWORD, DB_HOST, DATABASE_NAME)


class ProductionConfig(Config):
    DEBUG = False
    DB_USERNAME = os.environ.get('DB_USERNAME')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_HOST = os.environ.get('DB_HOST')
    DATABASE_NAME = os.environ.get('DATABASE_NAME')
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://%s:%s@%s:3306/%s?charset=utf8" % (DB_USERNAME, DB_PASSWORD, DB_HOST, DATABASE_NAME)
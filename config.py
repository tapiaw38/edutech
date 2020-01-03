import os


class Config(object):
    SECRET_KEY = 'my_secret_key'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_SSL = False
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'tapiaw38@gmail.com'
    MAIL_PASSWORD = 'Walter153294'

class DevelopmentConfig(Config):
    DEBUG = True
    dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"
    SQLALCHEMY_DATABASE_URI = dbdir
    SQLALCHEMY_TRACK_MODIFICATIONS = False

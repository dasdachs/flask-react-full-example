import os


class Config(object):
    SECRET_KEY = "8b57160a-6969-4dfd-ac71-e30455ff6301"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False


class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///inventory.db"


class TestingConfig(Config):
    DATABASE_URI = "sqlite:///:memory:"
    TESTING = True

from os import environ

class Config:
    SECRET_KEY = environ.get('SECRET_KEY', 'defaultSecretKey')
    DEBUG = environ.get('DEBUG', False)

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    DEBUG = True
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False

config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
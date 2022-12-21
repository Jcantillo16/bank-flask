import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dummy-key')
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


config_by_name = {
    'dev': DevelopmentConfig,
    'test': TestingConfig
}

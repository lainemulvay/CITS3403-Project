import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "SgUkXp2s5v8y/B?E"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'test.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class SeleniumConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('SELENIUM_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'selenium.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

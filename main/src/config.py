from os import getenv


class FlaskConfig(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = getenv("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class FlaskProductionConfig(FlaskConfig):
    DEBUG = False


class FlaskDevelopmentConfig(FlaskConfig):
    DEVELOPMENT = True
    DEBUG = True


class FlaskTestingConfig(FlaskConfig):
    TESTING = True

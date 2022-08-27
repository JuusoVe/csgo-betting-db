from os import getenv


class FlaskConfig:
    """
    Shared config for all environments."""

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = getenv("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class FlaskProductionConfig(FlaskConfig):
    """
    Production config,
    """

    DEBUG = False


class FlaskDevelopmentConfig(FlaskConfig):
    """
    Development config,
    """

    DEVELOPMENT = True
    DEBUG = True


class FlaskTestingConfig(FlaskConfig):
    """
    Testing config,
    """

    TESTING = True

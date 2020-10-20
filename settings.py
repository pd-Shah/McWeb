from os import (
    path,
    environ,
)

BASE_DIR = path.abspath(path.dirname(__file__))
DATABASE_DIR = path.join(BASE_DIR, "instance/")
DATABASE_NAME = ".sqlite"
PROXY_DLL = path.join(BASE_DIR, "dll\\Proxy.dll")
MISSION_TEMPLATE_DLL = path.join(BASE_DIR, "dll\\MissionTemplate.dll")
MTO_DLL_DIR = path.join(BASE_DIR, "dll\\MTO.dll")


class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = "sqlite:////" + DATABASE_DIR + DATABASE_NAME
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = environ.get(key="SECRET_KEY")
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    TESTING = True


configs = {
    "development": "settings.DevelopmentConfig",
    "testing": "settings.TestingConfig",
    "production": "settings.ProductionConfig",
}


config = configs[environ.get("FLASK_ENV", default="production")]

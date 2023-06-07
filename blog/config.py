import os


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "postgres://flask_yahe_user:t9kB6xMn4CTQLZ5KNSMNzznVbx61R7DJ@dpg-ci015qd269v5qbnbr73g-a.oregon-postgres.render.com/flask_yahe"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'e+%_r$h4aui+vw_jn^!3)&pk6v=i-3!&dcy07i6x@97gf#-osc'
    WTF_CSRF_ENABLED = True
    FLASK_ADMIN_SWATCH = 'cosmo'
    OPENAPI_URL_PREFIX = '/api/swagger'
    OPENAPI_SWAGGER_UI_PATH = '/'
    OPENAPI_SWAGGER_UI_VERSION = '3.22.0'


class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")


class TestingConfig(BaseConfig):
    TESTING = True

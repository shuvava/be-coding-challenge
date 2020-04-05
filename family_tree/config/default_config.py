# -*- coding: utf-8 -*-


class DefaultConfig(object):
    VERSION: str = '0.0.0.1'
    APP_NAME: str = 'sample app'

    # Flask settings
    DEBUG: bool = False
    SERVER_NAME: str = '127.0.0.1:5000'

    # Flask-Restplus settings
    SWAGGER_UI_JSONEDITOR: bool = True
    SWAGGER_UI_DOC_EXPANSION: str ='list'
    RESTPLUS_VALIDATE: bool = True
    RESTPLUS_MASK_SWAGGER: bool = False
    RESTPLUS_ERROR_404_HELP: bool = False

    # SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI: str = 'postgres://family:P@ssw0rd@127.0.0.1:5432/family'
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
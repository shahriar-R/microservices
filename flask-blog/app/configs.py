import os


class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = '15109ef2c061a02c6aa48e5b1927c69b0f77d3e58237946d66e050cf245d2e42'
    SECRET_KEY = 'a4ef30e752eb8e28eedb1dffe81ec7ac903fb53b6cb1c052e9257251e8a3178f'

class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = ...

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(Config.BASE_DIR, 'app.db')
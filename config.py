import os

class Config(object):
    DEBUG = False
    LOGGING_PATH = os.getenv('LOGGING_PATH', 'python_logging/logging.yaml')

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+pg8000://scrum-progress:scrum-progress@localhost/scrum-progress'
    DEBUG = True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+pg8000://scrum-progress:scrum-progress@localhost/scrum-progress'
    DEBUG = True

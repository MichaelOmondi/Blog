import os




class Config:
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY='secret'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:access@localhost/pitches'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #  email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
    
class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
   
class TestConfig(Config):
    '''
    Testing configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:access@localhost/pitches'

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:access@localhost/pitches'
    
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}


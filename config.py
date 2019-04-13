import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL = ''
    NEWS_API_KEY = ''
    SECRET_KEY = os.urandom(32)

class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development': DevcConfig,
'production': ProdConfig
}

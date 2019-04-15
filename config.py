import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey='
    NEWS_API_KEY = '753878d6347e4c429217670dfc2e0ee5'

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
'development': DevConfig,
'production': ProdConfig
}

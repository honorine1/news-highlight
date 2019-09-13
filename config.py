import os

class Config:
    '''
    General configuration parent class
    '''

    NEWS_API_BASE_URL = 'https://newsapi.org/v2/{}?apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRETE_KEY = os.environ.get('SECRETE_KEY')


class ProdConfig(Config):
    '''
    production configuration child class
        Args:
            Config: the parent configuration class with general configuration settings
    '''
    pass


class DevConfig(Config):

    '''
    development configuration child class
    args:
        Config: the parent configuration class with general configuration settings
    '''
    DEBUG = True

config_options = {            #########to help us access different configuration option classes.
'development':DevConfig,
'production': ProdConfig

}



    
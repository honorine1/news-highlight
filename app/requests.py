# from app import app
import urllib.request,json # module that will help us create a connection to our API URL and send a request
from .models import Source

# Getting api key
api_key = None
# Getting the source base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

# Source = source.Movie
#getting api key
# api_key = app.config['NEWS_API_KEY']

#getting the source base url
# base_url = app.config['NEWS_API_KEY']

def get_source(category):
    '''
    function that gets the json response to our url request
    '''
    get_source_url = base_url.format(category,api_key)
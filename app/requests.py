# from app import app
import urllib.request,json # module that will help us create a connection to our API URL and send a request
from .models import Source,Article

# Getting api key
api_key = None
# Getting the source base url
base_url = None
article_url = None


def configure_request(app):
    global api_key,base_url,article_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    article_url = app.config['ARTICLES_API_BASE_URL']

def get_sources(category):
    '''
    function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_sources = None

        if get_sources_response['sources']:
            source_sources_list= get_sources_response['sources']
            source_sources = process_sources(source_sources_list)

    return  source_sources

def process_sources(source_list):
    '''
    function that processes the movie result and transform them to a list of objects
    args:
        source_list: A list of dictionaries that contain source details
    returns:
        source_sources: a list of source objects
    '''

    source_sources =[]
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        name = source_item.get('name')
        url = source_item.get('url')
        category = source_item.get('category')
        country = source_item.get('country')

        if name:

            source_object=Source(id,name,description,url,category,country)
            source_sources.append(source_object)
    return source_sources


def get_article(id):
    get_article_details_url = article_url.format(id,api_key)
    print(get_article_details_url)

    with urllib.request.urlopen(get_article_details_url) as url:
        get_article_details_data = url.read()
        get_article_details_response = json.loads(get_article_details_data)

        article_object = None
        if get_article_details_response['articles']:
            article_articles_list= get_article_details_response['articles']
            article_articles = process_article(article_articles_list)

    return  article_articles
    
def process_article(article_list):
    '''
    function that processes the article result and transform them to a list of objects
    args:
        article_list: A list of dictionaries that contain articlee details
    returns:
        article_resultss: a list of article objects
    '''

    article_articles =[]
    for article_item in article_list:
        title = article_item.get('title')
        description = article_item.get('description')
        author = article_item.get('author')
        url = article_item.get('url')
        urlToImage =  article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
      
        if urlToImage:
            article_object=Article(author, title, description, url, urlToImage, publishedAt)
            article_articles.append(article_object)

    return article_articles



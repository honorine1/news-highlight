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
    get_article_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_article_details_url) as url:
        get_article_details_data = url.read()
        get_article_details_response = json.loads(article_details_data)

        article_object = None
        if get_article_details_response:
            id = article_details_response.get('id')
            title = article_details_response.get('title')
            author = article_details_response.get('author')
            url = article_details_response.get('url')
            publishedAt = article_details_response.get('publishedAt')
        
            article_object = article(id,title,author,url,publishedAt)



# def get_source(id):
#     get_source_details_url = base_url.format(id,api_key)

#     with urllib.request.urlopen(get_source_details_url) as url:
#         source_details_data = url.read()
#         source_details_response = json.loads(source_details_data)

#         source_object = None
#         if movie_details_response:
#             id = source_details_response.get('id')
#             name = source_details_response.get('original_name')
#             description = movie_details_response.get('description')
#             url = movie_details_response.get('url')
#             category = movie_details_response.get('category')
#             country = movie_details_response.get('country')

#             source_object = Source(id,name,description,url,category,country)

# return source_object            
         

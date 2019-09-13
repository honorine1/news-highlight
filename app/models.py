class Source:
    '''
    Source class to define source objects
    '''

    def __init__(self,id, name, description, url, category,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country

class Article:
    '''
    arcticle class to define article object
    '''

    def __init__(self, author, title, description, url, urlToImage, publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.url = urlToImage
        self.publishedAt = publishedAt

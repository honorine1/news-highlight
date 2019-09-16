from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_article

# from ..requests import get_sources,get_source,search_source
# from .form import ReviewForm
# from ..models import Review
# from app import app

#views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    # getting general news
    general = get_sources('general')
    # entertainment = get_sources('entertainment')
    # sport = get_sources('sport')
    # technology = get_sources('technology')
    # print(general)
    title = 'News - welcome to this news platform'
    return render_template('index.html',title = title,  general = general )

@main.route('/article/<id>')
def article(id):

    '''
    view article page function that returns the article details page and its data
    '''

    articles = get_article(id)
    print('hellll')
    print(articles)
    return render_template('article.html',articles = articles)
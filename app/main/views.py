from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_source
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
    title = 'News - welcome to this news platform'
    return render_template('index.html',title = title)

# if __name__ == '__main__':
#     app.run(Debug = True )
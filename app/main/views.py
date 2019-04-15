from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_news_source

# views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    title = "Hello I work"
    sources = get_news_source()
    return render_template('index.html', title = title, source=sources)

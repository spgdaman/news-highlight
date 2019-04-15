from flask import render_template, request, redirect, url_for
from . import main, get_news_source

# views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    title = "<h1>Hello I work</h1>"
    sources = get_news_source("general")
    return render_template('index.html', title = title)

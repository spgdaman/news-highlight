from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_news_source, get_articles

# views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    title = "Hello I work"
    sources = get_news_source()
    return render_template('index.html', title = title, source=sources)

@main.route('/articles/<string:article_id>')
def articles(article_id):
    articles = get_articles(article_id)
    return render_template('articles.html', articles=articles)

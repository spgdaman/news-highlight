from flask import render_template, request, redirect, url_for


# views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    title = "<h1>Hello I work</h1>"

    return render_template('index.html', title = title)

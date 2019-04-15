import urllib.request, json

# Getting api key
api_key = None

# Getting the base url
base_url = None

def configure_request(app):
    global api_key, base_url
    api_key = main.config['NEWS_API_KEY']
    base_url = main.config['NEWS_API_BASE_URL']

def get_news_source(category):
    get_base_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_base_url) as url:
        get_url_data = url.read()
        get_url_response =  json.loads(get_url_data)

        results = None

        if get_url_response['sources']:
            results_list = get_url_response['sources']
            results = process_results(results_list)

    return results

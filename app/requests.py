import urllib.request, json
from . import Source

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the base url
base_url = app.config['NEWS_API_BASE_URL']

def get_news_source():
    get_base_url = base_url.format(api_key)

    with urllib.request.urlopen(get_base_url) as url:
        get_url_data = url.read()
        get_url_response =  json.loads(get_url_data)

        results = None

        if get_url_response['sources']:
            results_list = get_url_response['sources']
            results = process_results(results_list)

    return results

def process_results(source_list):
    source_result = []

    for source in source_list:
        id = source.get("id")
        name = source.get("name")
        description = source.get("description")
        url = source.get("url")
        category = source.get("category")
        langiage = source.get("language")
        country = source.get("country")

        source_object = Source(id,name,description,url,category,language,country)
        source_result.append(source_object)

    return source_result

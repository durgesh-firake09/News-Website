import requests
import json


def getData(category):
    with open('config.json', 'r') as configFile:
        params = json.load(configFile)['params']
        configFile.close()

    if category == 'All':
        category = ''
    url = r'https://newsapi.org/v2/top-headlines?country=in&category=' + category.lower()+'&apiKey=' + params["apiKey"]
    r = requests.get(url)
    return r.json()['articles']





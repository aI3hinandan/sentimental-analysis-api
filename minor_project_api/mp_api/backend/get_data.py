import datetime

from newsapi import NewsApiClient

from .sentiment_analysis import analyzeNews


def getRecentNews(query):
    api = NewsApiClient(api_key='059682eeb50c491f9dac805324edfad1')
    tm = datetime.datetime.today() - datetime.timedelta(days=3)
    result = api.get_everything( qintitle=query,from_param= tm.date().isoformat())
    return analyzeNews(result)

def getLiveNews(query):
    api = NewsApiClient(api_key='059682eeb50c491f9dac805324edfad1')
    result = api.get_top_headlines(qintitle=query)
    return analyzeNews(result)
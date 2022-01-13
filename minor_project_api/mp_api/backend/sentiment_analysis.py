from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize
import pandas as pd
import numpy as np
import os

def analyzeNews(newsDict):
    sid = SentimentIntensityAnalyzer()
    articles = newsDict['articles']
    scores = [sid.polarity_scores(article['description']) for article in articles]
    final_avg = {index: (sum([score[index] for score in scores])/len(scores) if len(scores) > 0 else 0) for index in ('neg','neu', 'pos', 'compound')}
    return final_avg
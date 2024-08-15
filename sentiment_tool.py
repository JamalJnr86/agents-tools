#sentiment_tool.py
from textblob import TextBlob #type: ignore

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return "The sentiment is positive."
    elif sentiment < 0:
        return "The sentiment is negative."
    else:
        return "The sentiment is neutral."

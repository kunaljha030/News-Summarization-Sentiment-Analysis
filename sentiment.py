from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    return "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"

def analyze_comparative_sentiment(articles):
    sentiments = {"Positive": 0, "Negative": 0, "Neutral": 0}
    for article in articles:
        sentiment = analyze_sentiment(article['summary'])
        sentiments[sentiment] += 1
    return sentiments

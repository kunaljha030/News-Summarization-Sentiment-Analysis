from fastapi import FastAPI, Query
from scraper import fetch_news
from sentiment import analyze_comparative_sentiment
from tts import text_to_speech

app = FastAPI()

@app.get("/news")
def get_news(company: str = Query(..., title="Company Name")):
    articles = fetch_news(company)
    sentiment_analysis = analyze_comparative_sentiment(articles)

    # Convert sentiment summary to speech
    tts_filename = text_to_speech(str(sentiment_analysis), "sentiment.mp3")

    return {"articles": articles, "sentiment_analysis": sentiment_analysis, "tts_file": tts_filename}

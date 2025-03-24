# News-Summarization-Sentiment-Analysis
News Summarization &amp; Sentiment Analysis


##  Overview
This project fetches company news, summarizes, analyzes sentiment, and generates an audio summary in Hindi.

**Create a virtual environment**
python -m venv env
source env/bin/activate   # For Mac/Linux
.\env\Scripts\activate

**Install dependencies:**
pip install -r requirements.txt

**Start the FastAPI backend:**
uvicorn app:app --reload 

**Run the Streamlit app:**
streamlit run frontend.py

**Features**
Fetches live news for any company
Summarizes articles
Performs sentiment analysis
Extracts topics from summaries
Generates Hindi audio summary

**Future Improvements**
Multilingual support
Advanced sentiment models
Enhanced UI with charts and graphs





import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/news"

#
def main():
    st.title("News Summarization & Sentiment Analysis")
    company_name = st.text_input("Enter Company Name")
    
    if st.button("Fetch News"):
        response = requests.get(API_URL, params={"company": company_name})
        data = response.json()

        if not data['articles']:
            st.error("No news found.")
            return
        
        for article in data['articles']:
            st.subheader(article['title'])
            st.write(article['summary'])
            st.write(f"[Read more]({article['link']})")

        st.subheader("Sentiment Analysis")
        st.json(data['sentiment_analysis'])

        # Play TTS audio
        st.audio("sentiment.mp3")

if __name__ == "__main__":
    main()

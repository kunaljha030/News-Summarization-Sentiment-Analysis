import requests
from bs4 import BeautifulSoup

def fetch_news(company_name):
    query = company_name.replace(" ", "+")
    url = f"https://news.google.com/search?q={query}&hl=en&gl=US&ceid=US%3Aen"
    response = requests.get(url)

    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    articles = []

    for item in soup.find_all('article')[:10]:  # Ensure at least 10 articles
        try:
            title = item.find('h3').get_text() if item.find('h3') else ''
            summary = item.find('span').get_text() if item.find('span') else ''
            link = item.find('a')['href']
            if not link.startswith('http'):
                link = 'https://news.google.com' + link

            articles.append({"title": title, "summary": summary, "link": link})
        except Exception as e:
            print("Error scraping article:", e)

    return articles

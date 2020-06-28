from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.cnn.com/world/live-news/coronavirus-pandemic-06-27-20-intl/index.html").text
soup = BeautifulSoup(source, 'lxml')
articles = []

for article in soup.find_all('article', class_ = "sc-jqCOkK sc-kfGgVZ hQCVkd"):
    headline = article.header.h2.text
    articles.append(headline)
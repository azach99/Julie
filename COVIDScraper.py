from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.worldometers.info/coronavirus/").text
soup = BeautifulSoup(source, 'lxml')
worldwide_list = []

source_2 = requests.get("https://www.worldometers.info/coronavirus/country/us/").text
soup_2 = BeautifulSoup(source_2, 'lxml')
us_list = []


for art in soup.find_all('div', class_ = "maincounter-number"):
    number = art.span.text
    worldwide_list.append(number)

for article in soup_2.find_all('div', class_ = "maincounter-number"):
    number = article.span.text
    us_list.append(number)

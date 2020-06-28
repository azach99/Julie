from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.msn.com/en-us/weather").text
soup = BeautifulSoup(source, 'lxml')
#print(soup.prettify())

article = soup.find('div', class_ = "current-info")
#print(article.prettify())

temperature = article.span.text
#print(temperature)

art = soup.find('div', class_ = "weather-info")
#print(art.prettify())

#print(art.span.text)
feeling = art.span.text

output = "the current condition is {} and the temperature is {} degrees".format(feeling, temperature)


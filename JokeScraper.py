from bs4 import BeautifulSoup
import requests

source = requests.get("http://www.laughfactory.com/jokes/popular-jokes/all-time").text
soup = BeautifulSoup(source, 'lxml')
joke_list = []

source_2 = requests.get("http://www.laughfactory.com/jokes/popular-jokes/all-time/2").text
soup_2 = BeautifulSoup(source_2, 'lxml')

source_3 = requests.get("http://www.laughfactory.com/jokes/popular-jokes/all-time/3").text
soup_3 = BeautifulSoup(source_3, 'lxml')

source_4 = requests.get("http://www.laughfactory.com/jokes/popular-jokes/all-time/4").text
soup_4 = BeautifulSoup(source_4, 'lxml')


for article in soup.find_all('div', class_ = "joke-text"):
    joke = article.p.text
    joke_list.append(joke)



for arti in soup.find_all('div', class_ = "joke-text"):
    joke = arti.p.text
    joke_list.append(joke)



for art in soup.find_all('div', class_ = "joke-text"):
    joke = art.p.text
    joke_list.append(joke)



for a in soup.find_all('div', class_ = "joke-text"):
    joke = a.p.text
    joke_list.append(joke)





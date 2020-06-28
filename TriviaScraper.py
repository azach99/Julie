from bs4 import BeautifulSoup
import requests
from Question import Question
from QuestionSet import QuestionSet

source = requests.get("https://www.triviaquestionss.com/general-trivia-questions/").text
soup = BeautifulSoup(source, 'lxml')
set = QuestionSet()

for article in soup.find_all('div', class_ = "otw-sc-toggle"):
    question = article.h3.text
    answer = article.p.text
    set.add_question(question, answer)

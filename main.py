import speech_recognition as sr
import pyttsx3
import random
from datetime import datetime
from Scraper import articles
from TriviaScraper import set
from JokeScraper import joke_list
from WeatherScraper import output
from COVIDScraper import worldwide_list, us_list

r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.say("hello")
loop = True

def ask_questions():
    q_set = set
    points = 0
    i = 0
    while i < 10:
        n = random.randint(0, set.num_of_entries - 1)
        inquire = set.get_list()[n].get_question()
        engine.say(inquire)
        engine.runAndWait()
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            text = text.lower()
            print(text)
            if (str(text)) == str(set.get_list()[n].get_answer()):
                engine.say("Correct")
                points += 10
            else:
                engine.say("Incorrect {}".format(set.get_list()[n].get_answer()))
            i += 1
        except sr.UnknownValueError:
            print("Could not understand you")
    engine.say("you earned {} points".format(points))

def tell_joke():
    n = random.randint(0, len(joke_list) - 1)
    out = joke_list[n]
    engine.say(out)

def tell_articles():
    article_list = articles
    for i in range(1):
        n = random.randint(0, len(article_list) - 1)
        art = article_list[n]
        engine.say(art)

while (loop):
    with sr.Microphone() as source:
        print("Say Anything: ")
        engine.runAndWait()
        audio = r.listen(source)
        print("achieved")
        text = r.recognize_google(audio)
        text = text.lower()
        print("You said: {}".format(text))
        if str(text) == str("quit") or str(text) == str("stop") or str(text) == str("quit quit"):
            loop = False
        if str(text) == str("hey julie"):
            engine.say("yes?")
            condition = True
            while (condition):
                with sr.Microphone() as source:
                    engine.runAndWait()
                    audio = r.listen(source)
                    try:
                        text = r.recognize_google(audio)
                        text = text.lower()
                        print("You said: {}".format(text))
                        if str(text) == str("what is today's date"):
                            engine.say(datetime.date(datetime.now()))
                        if str(text) == str("play trivia"): #use some webscraping with this
                            ask_questions()
                        if str(text) == str("thanks"):
                            condition = False
                        if str(text) == str("tell me a joke"):
                            tell_joke()
                        if str(text) == str("tell me the news"):
                            tell_articles()
                        if str(text) == str("tell me the weather"):
                            engine.say(output)
                        if str(text) == str("tell me coronavirus statistics"):
                            engine.say("worldwide cases: {}".format(worldwide_list[0]))
                            engine.say("worldwide deaths: {}".format(worldwide_list[1]))
                            engine.say("united states cases: {}".format(us_list[0]))
                            engine.say("united states deaths: {}".format(us_list[1]))
                        if str(text) == str("what time is it"):
                            if (datetime.now().hour > 12 and datetime.now().hour < 24):
                                engine.say(datetime.now().hour - 12)
                                engine.say(datetime.now().minute)
                                engine.say("pm")
                            elif datetime.now().hour == 12:
                                engine.say(datetime.now().hour)
                                engine.say(datetime.now().minute)
                                engine.say("pm")
                            elif datetime.now.hour == 24:
                                engine.say("12")
                                engine.say(datetime.now().minute)
                                engine.say("am")
                            else:
                                engine.say(datetime.now().hour)
                                engine.say(datetime.now().minute)
                                engine.say("am")
                    except sr.UnknownValueError:
                        print("Sorry could not hear you")
        if str(text) == str("hello"):
            engine.say("hi zach")



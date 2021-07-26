import requests
from ss import *
import json
import pyttsx3


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

api_address = "http://newsapi.org/v2/top-headlines?country=us&apikey="+api_store().key("newsapi")
json_data = requests.get(api_address).json()

ar = []


def news():
    for i in range(3):
        ar.append("Number " + str(i+1) + ": " + json_data["articles"][i]["title"]+".")

    return ar


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def speak_news():
    url = 'http://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey='+api_store.key("newsapi")
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    speak('Source: The Times Of India')
    speak('Todays Headlines are..')
    for index, articles in enumerate(arts):
        speak(articles['title'])
        if index == len(arts)-1:
            break
        speak('Moving on the next news headline..')
    speak('These were the top headlines, Have a nice day Sir!!..')


def getNewsUrl():
    return 'http://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey='+api_store.key("newsapi")


arr = news()

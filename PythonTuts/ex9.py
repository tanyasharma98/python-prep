#Akhbaar padkeeeee Sunaoooooo
#install ------- pip install pywin32
import json

import requests


def speak(str):
    from win32com.client import Dispatch
    Windows_Speak = Dispatch('SAPI.Spvoice')
    # Windows_Speak.Speak(f"Lets begins with today's news")
    Windows_Speak.Speak(str)


if __name__ == '__main__':
    # speak("pagl ka bache nikal yaha se")
    # url ="https://newsapi.org/v2/sources?apiKey=API_KEY"
    # 
    # x= requests.get(url)
    # print(x.text)
    url ="https://newsapi.org/v2/top-headlines?country=us&apiKey=17c5a8dfd2684d2c8189d0c2b4da16b6"
    x=requests.get(url)
    f=x.text
    parsed = json.loads(f)
    print(parsed)
    news = parsed['articles']
    speak(f"Lets begins with Current news")
    for article in news:
        speak(article['title'])
        speak("Moving to the next news...")

    # for i in range(0,20):
    #     speak(parsed['articles'][i]['title'])

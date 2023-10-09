import pyttsx3
import requests
import speech_recognition as sr
import datetime
from bs4 import BeautifulSoup




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good morning NASA Crew!")
        

    elif hour>=12 and hour<18:
        speak("Good afternoon NASA Crew!")
        

    else:
        speak("Good night NASA Crew!")
        
        



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en-es')
        print(f"The user said: {query}\n")

    except Exception as e:
        print("Say it again please...")
        return "None"
    return query

if __name__== "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            greetMe()


            while True:
                query = takeCommand().lower()
                if "Go" in query:
                    speak("Call me if you need me")
                    break

                elif "hello" in query:
                    speak("Hi, how are you?")
                
             
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)



                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                elif "temperature" in query:
                    search = "temperature in San jose iturbide guanajuato"
                    url = f"https://www.google.com.mx/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div",class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "temperature in San jose iturbide guanajuato"
                    url = f"https://www.google.com.mx/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div",class_ = "BNeaWE").text
                    speak(f"current{search} is {temp}")

                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"The time is {strTime}")
                elif "finally sleep" in query:
                    speak("Going to sleep")
                    exit()
    
from unittest import result
import webbrowser
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Entendiendo...")
        query = r.recognize_google(audio, language='en-es')
        print(f"The user said: {query}\n")

    except Exception as e:
        print("Say it again please...")
        return "None"
    return query

query = takeCommand().lower()  

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("STAR","")
        query = query.replace("google search","")
        query = query.replace("google","")
        speak("This is what i found on google")

    try:
        pywhatkit.search(query)
        result = googleScrap.summary(query,1)
        speak(result)

    except:
        speak("Not available")

def searchYoutube(query):
    if "youtube" in query:
        speak("What i found for your search!")
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        query = query.replace("jarvis","")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Listo, señorita")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Looking from wikipedia...")
        query = query.replace("wikipedia","")
        query = query.replace("search wikipedia","")
        query = query.replace("jarvis","")
        results = wikipedia.summary(f'{query}', sentences=2)
        speak("According wikipedia...")
        print(results)
        speak(results)
      

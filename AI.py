import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak('Good Morning Sir!')
    elif hour>12 and hour<18:
        speak('Good Afternoon Sir!')
    else:
        speak('Good Evening Sir')
    speak('I am Jarvis , Pleased to meet you')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio ,language='en-in')
        active = r.recognize_google(audio , language='en-in')
        print(f"User Said : {query} \n")
    except Exception as e:
        print("Say that again please....")
        return "None"
    return query
class Browser:
    chrome = 'C:\Aniket\AppData\Local\Google\Chrome\Application\chrome.exe %s'
    pass
webbrowser.register('chrome',None ,
webbrowser.BackgroundBrowser('C:\\Users\\Aniket\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe %s'))
if __name__ == '__main__':
    speak("Hello")
    wishMe()
    while(True):
        query = takeCommand().lower()

        if 'wikipedia' in query:
            print('Searching Wikipedia.....')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query,sentences = 2)
            speak("According to wikipedia...")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            print("Opening Youtube.....")
            webbrowser.open("www.youtube.com")

        elif "search" in query:
            query =  query.replace("search","")
            webbrowser.open(f"www.google.com/search?q={query}")

        elif 'youtube' in query:
            query = query.replace("youtube", "")
            webbrowser.open(f"www.youtube.com/results?search_query={query}")

        elif 'jarvis' in query:
            speak("Yes Sir , How may i help you?")


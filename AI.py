import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
newVoiceRate = 145
engine.setProperty('rate',newVoiceRate)

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
        speak('Good Evening Sir!')
    speak('I am Jarvis , Pleased to meet you ')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.adjust_for_ambient_noise(source)
        r.dynamic_energy_threshold = True
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio ,language='en-in')
        print(f"User Said : {query} \n")
    except Exception as e:
        print("Say that again please....")
        return "None"
    return query

def jarvis():
    speak("All Functions Activated...")
    while (True):
        query = takeCommand().lower()

        if 'open youtube' in query:
            print("Opening Youtube.....")
            speak("Yes Sir , Your wish is my command")
            speak("Opening Youtube...")
            webbrowser.open("www.youtube.com")

        elif "search" in query:
            query = query.replace("search", "")
            speak("Yes Sir , Your wish is my command")
            speak(f"Searching about {query}....")
            webbrowser.open(f"www.google.com/search?q={query}")

        elif 'youtube' in query:
            query = query.replace("youtube", "")
            speak("Yes Sir , Your wish is my command")
            speak(f"Searching in Youtube about {query}....")
            webbrowser.open(f"www.youtube.com/results?search_query={query}")

        elif 'deactivate' in query:
            speak("Thank You Sir , Wish you a Good Day!")
            break

        elif 'jarvis' in query:
            speak("Yes Sir , How may i help you?")


class Browser:
    chrome = 'C:\Aniket\AppData\Local\Google\Chrome\Application\chrome.exe %s'
    pass
webbrowser.register('chrome',None ,
webbrowser.BackgroundBrowser('C:\\Users\\Aniket\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe %s'))
if __name__ == '__main__':
    wishMe()
    while(True):
        query = takeCommand().lower()
        if 'activate' in query:
            speak("Activating Sir....")
            jarvis()
        if 'shutdown' in query:
            speak("Shutting Down All Systems...")
            break





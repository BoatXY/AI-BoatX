import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
from playsound import playsound
import os
import random
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
newVoiceRate = 145
engine.setProperty('rate',newVoiceRate)

os.chdir(os.path.dirname(os.path.abspath(__file__)))
c_dir = os.getcwd()

def remove(string):
    return string.replace(" ", "")

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
        r.adjust_for_ambient_noise(source,duration=0.5)
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

def jarvis_func():
    playsound(f"{c_dir}\\Jarvis Voice\\allfunc.mp3")
    while (True):
        query = takeCommand().lower()


        if 'open youtube' in query:
            print("Opening Youtube.....")
            playsound(f"{c_dir}\\Jarvis Voice\\urwish.mp3")
            speak("Opening Youtube...")
            webbrowser.open("www.youtube.com")

        elif "search" in query:
            query.replace("jarvis","")
            query = query.replace("search", "")
            playsound(f"{c_dir}\\Jarvis Voice\\urwish.mp3")
            speak(f"Searching about {query}....")
            pywhatkit.search(query)

        elif 'youtube' in query:
            query = query.replace("jarvis","")
            query = query.replace("youtube", "")
            playsound(f"{c_dir}\\Jarvis Voice\\urwish.mp3")
            speak(f"Searching in Youtube about {query}....")
            pywhatkit.playonyt(query)

        elif 'music' in query:
            query = query.replace("music", "")
            query = remove(query)
            lis3 = os.listdir(f"{c_dir}\\music")
            rup = random.choice(lis3)
            playsound(f"{c_dir}\\Jarvis Voice\\urwish.mp3")
            try:
                os.startfile(f"{c_dir}\\music\\{query}.mp3")
            except Exception as e:
                speak("Sorry , please say the name correctly")

        elif 'open' in query:
            query = query.replace("open", "")
            query = remove(query)
            lis3 = os.listdir(f"{c_dir}\\exe")
            rup = random.choice(lis3)
            playsound(f"{c_dir}\\Jarvis Voice\\urwish.mp3")
            try:
                os.startfile(f"{c_dir}\\exe\\{query}.exe.lnk")
            except Exception as e:
                speak("Sorry , Please say again")
        
        elif 'web' in query:
            query = query.replace("web","")
            query = remove(query)
            playsound(f"{c_dir}\\Jarvis Voice\\urwish.mp3")
            webbrowser.open(f"www.{query}.com")

        elif 'deactivate' in query:
            playsound(f"{c_dir}\\Jarvis Voice\\thank.mp3")
            break

        elif 'jarvis' in query:
            playsound(f"{c_dir}\\Jarvis Voice\\help.mp3")


class Browser:
    chrome = 'C:\Aniket\AppData\Local\Google\Chrome\Application\chrome.exe %s'
    pass
webbrowser.register('chrome',None ,
webbrowser.BackgroundBrowser('C:\\Users\\Aniket\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe %s'))
if __name__ == '__main__':
    playsound(f"{c_dir}\\Jarvis Voice\\startup.mp3")
    while(True):
        query = takeCommand().lower()
        if 'wake up jarvis' in query:
            playsound(f"{c_dir}\\Jarvis Voice\\activate1.mp3")
            jarvis_func()
        if 'dismiss' in query:
            playsound(f"{c_dir}\\Jarvis Voice\\shut.mp3")
            break
input()





import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
#import pyaudio
import os
import webbrowser
import playsound
import pyautogui
import psutil
import pyjokes
pk = pyttsx3.init('sapi5')
voices=pk.getProperty('voices')
pk.setProperty('voice',voices[0] or [1].id)
def speak(audio):
    pk.say(audio)
    pk.runAndWait()

speak("this is AI Voice Assistant")


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(f"The current time is:")
    speak(Time)


time()


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is:")
    speak(date)
    speak(month)
    speak(year)


date()


def wishme():
    speak("Welcome back mam ")
    #time()
    #date()
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <= 12:
        speak("Good Morning ")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon ")
    elif hour >= 12 and hour <= 24:
        speak("Good Evening ")
    else:
        speak("Good Night")
    speak("AI in your service! How can i help you?")


#wishme()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio)
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please..")

        return "None"
    return query

def screenshot():
    img = pyautogui.screenshot()
    img.save(r"C:\Users\hp\OneDrive\Desktop\Prashansa\ss.jpg", encoding= 'utf-8')

def cpu():
    usage= str(psutil.cpu_percent())
    speak("CPU is at" + usage)

    battery= psutil.sensors_battery()
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    wishme()


while True:
    query = takeCommand().lower()
    print(query)

    if "time" in query:
        time()
    elif "date " in query:
        date()
    elif "offline" in query:
        quit()
    elif " wikipedia" in query:
        speak("Searching......")
        print("Searching......")
        query = query.replace("wikipedia", "")
        try:
         result = wikipedia.summary(query , sentences=2)
         speak(result)
         print(result)
        except wikipedia.exceptions.PageError:
            pass
    elif "logout" in query:
        os.system("shutdown - 1 ")
    elif "shutdown" in query:
        os.system("shutdown /s /t 1 ")
    elif "restart" in query:
        os.system("shutdown /r /t 1 ")

    elif 'who are you' in query or 'what can you do' in query:
        speak('I am AI your personal assistant. I am programmed to minor tasks like'
              'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia'
              'get top headline news from times of india and')

    elif "who made you" in query or "who created you" in query or "who discovered you" in query:
        speak("I was created by [Your Name] using Python programming language.")

        #elif "who made you" in query or "who created you" in query or "who discovered you" in query:

        pass  # Placeholder, you can add code here if needed

    elif 'open stack' in query:

        webbrowser.open("https://stackoverflow.com")
    elif 'open youtube' in query:
        webbrowser.open("https://www.youtube.com")


    elif 'news' in query:
        news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/defaultinterstitial.cms")
        speak('Here are some headlines from the Times of India,Happy reading')
    elif "remember that" in query:
        speak("What should i remember")
        data = takeCommand()
        speak("you said me to remember" + data)
        remember = open("data.txt", "w")
        remember.write(data)
        remember.close()

    elif "screenshot" in query:
        screenshot()
        speak("done")
    elif "cpu" in query:
        cpu()

    elif "joke" in query:
        jokes()



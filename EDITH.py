import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import pyautogui
from time import sleep


engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    print("The current time is ", Time)


def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)
    print("The current date is " + str(day) + "/" + str(month) + "/" + str(year))


def greet_me():
    print("Welcome back sir!!")
    speak("Welcome back sir!!")

    hour = datetime.datetime.now().hour
    if hour >= 4 and hour < 12:
        speak("Good Morning")
        print("Good Morning")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon ")
        print("Good Afternoon")
    elif hour >= 16 and hour < 24:
        speak("Good Evening")
        print("Good Evening")
    else:
        speak("Good Night")
        print("Good Night")

    speak("EDITH at your service sir, please tell me how may I help you.")
    print("EDITH at your service sir, please tell me how may I help you.")


def screenshot():
    img = pyautogui.screenshot()
    img.save("screenshot.png")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 1900
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)

    except Exception as error:
        print(error)
        speak("Please say that again")
        return "Try Again"

    return query

def spotify():
    try:
        speak("What song do you want to play Sir ")
        song = takecommand()
        wb.open(f"https://open.spotify.com/search/{song}")
        sleep(11)
        speak(f"Playing{song} music on spotify")
        print("Playing music on spotify")
        pyautogui.click(x=900, y=320)

        quit()

    except Exception as e:
        speak("Can't open now, please try again later.")
        print("Can't open now, please try again later.")


"""def prime():
    try:
        speak("What do you want to see ")
        movie = takecommand()
        wb.open(f"https://www.primevideo.com/search/{movie}")
        sleep(6)
        speak(f"Playing{movie} ")
        print(f"Playing {movie}")
        pyautogui.click(x=60, y=200)

        quit()
    except Exception as error:
        speak("cant undestand please say that again")"""



if __name__ == "__main__":
    greet_me()
    while True:
        query = takecommand().lower()
        if "time" in query:
            time()

        elif "date" in query:
            date()


        elif "who are you" in query:
            speak("I'm EDITH created by Master. Amay and I'm a python voice assistant.")
            print("I'm EDITH created by Master. Amay and I'm a python voice assistant.")

        elif "how are you" in query:
            speak("I'm fine sir, What about you?")
            print("I'm fine sir, What about you?")

        elif "fine" in query:
            speak("Glad to hear that")
            print("Glad to hear that sir!!")

        elif "good" in query:
            speak("Glad to hear that")
            print("Glad to hear that sir!!")

        elif "wikipedia" in query:
            try:
                speak("I'm searching...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except:
                speak("Can't find this page sir, please ask something else")

        elif "open youtube" in query:
            print("Opening Youtube")
            wb.open("youtube.com")


        elif "open google" in query:
            print("Opening google")
            wb.open("google.com")


        elif "open spotify" in query:
            wb.open("spotify.com")
            speak("opening spotify")



        elif "play music on spotify" in query:
            spotify()


        #elif "movies" in query:
         #   prime()



        elif "open youtube music" in query:
            wb.open("https://music.youtube.com/")


        elif "open Linkesin" in query:
            wb.open("Linkedin.com")

        elif "open stack overflow" in query:
            wb.open("stackoverflow.com")

        elif "open chrome" in query:
            chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)

        elif "search on chrome" in query:
            try:
                speak("What should I search?")
                print("What should I search?")
                chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                search = takecommand()
                wb.get(chromePath).open_new_tab(search)
                print(search)

            except Exception as e:
                speak("Can't open now, please try again later.")
                print("Can't open now, please try again later.")


        elif "take notes" in query:
            speak("What should I remember")
            data = takecommand()
            speak("You said me to remember that" + data)
            print("You said me to remember that " + str(data))
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "remember anything" in query:
            remember = open("data.txt", "r")
            speak("You told me to remember that" + remember.read())
            print("You told me to remember that " + str(remember))

        elif "screenshot" in query:
            screenshot()
            speak("I've taken screenshot, please check it")


        elif "offline" in query:
            speak("EDITH going offline")
            quit()


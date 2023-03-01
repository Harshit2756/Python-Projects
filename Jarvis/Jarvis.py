import pyttsx3  # pip install pyttsx3  == text data into speach
import datetime 
import speech_recognition as sr  # pip install speechRecognition == speach data into text

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getvoice(voice):
    voices = engine.getProperty('voices')
    # print(voices[1].id)
    if voice == 1:
        engine.setProperty('voice', voices[0].id)
    if voice == 2:
        engine.setProperty('voice', voices[1].id)

    speak("this is jarvis sir")

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("THe current time is")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    elif hour >= 18 and hour < 24:
        speak("Good Evening")
    else:
        speak("Good Night")

def wishme():
    speak("Welcome back sir!")
    greeting()
    speak("Jarvis at your service. Please tell me how can i help you?")

def takeCommandCMD():
    query = input("Command: ")
    return query

def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='Hi-IN')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please...")

        return "None"
    return query

if __name__ == "__main__":
    wishme()

    while True:
        query = takeCommandMic().lower()
        
        if 'time' in query:
            time()

        elif 'date' in query:
            date()


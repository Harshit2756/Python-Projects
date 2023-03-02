import pyttsx3  # pip install pyttsx3  == text data into speach
import datetime 
import speech_recognition as sr  # pip install speechRecognition == speach data into text

engine = pyttsx3.init()

# ********************* Speak Function ***********************
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# ********************* Vocie Change Function ***********************
def getvoice(voice):
    voices = engine.getProperty('voices')
    # print(voices[1].id)
    if voice == 1:
        engine.setProperty('voice', voices[0].id)
        speak("Hello sir to select my voice press 1")
    if voice == 2:
        engine.setProperty('voice', voices[1].id)
        speak("Hello sir to select my voice press 2")


    speak("this is jarvis sir")

# ********************* Time Function ***********************
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("THe current time is")
    speak(Time)

# ********************* Date Function ***********************
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

# ********************* Greeting Function ***********************
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

# ********************* Wishme Function ***********************
def wishme():
    speak("Welcome back sir!")
    greeting()
    speak("Jarvis at your service. Please tell me how can i help you?")

# ************ Take Command Through CMD Function *************
def takeCommandCMD():
    query = input("Command: ")
    return query

# ************ Take Command Through Mic Function *************
def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please...")

        return "None"
    return query

def quit():
    speak("Thanks for using me sir, have a good day.")
    exit()

# ********************* Main Function ***********************
if __name__ == "__main__":
    getvoice(1)
    wishme()

    while True:
        query = takeCommandMic().lower()
        
        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'Exit' in query:
            quit()
            


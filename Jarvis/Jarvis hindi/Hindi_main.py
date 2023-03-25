import pyttsx3  # pip install pyttsx3  == text data into speach
import datetime 
import speech_recognition as sr  # pip install speechRecognition == speach data into text

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='hi-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def wishme():
    speak("नमस्ते")
    speak("मैं आपकी सेवा में हूँ")

def TaskExe():
    while True:
        queryHindi = TakeCommand()

        if "नमस्ते" in queryHindi:
            speak("नमस्ते मेरा नाम जार्विस है")
            speak("मैं आपकी सेवा में हूँ")

TaskExe()
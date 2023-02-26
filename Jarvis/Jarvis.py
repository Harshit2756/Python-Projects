import pyttsx3  # pip install pyttsx3  == text data into speach

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def getvoice():
    voices = engine.getProperty('voices')
    # print(voices[1].id)
    if voices ==1:
        engine.setProperty('voice', voices[0].id)
    if voices == 2:
        engine.setProperty('voice', voices[1].id)

    speak =("this is jarvis sir")

while True:
    voices =int (input("Press 1 for male voice \n for female voice press 2 \n")) 
    # speak(audio)
    getvoice()
    voices = engine.getProperty('voices')

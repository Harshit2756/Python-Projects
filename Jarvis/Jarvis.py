import pyttsx3  # pip install pyttsx3  == text data into speach
import datetime # pip install datetime == get date and time
import speech_recognition as sr  # pip install speechRecognition == speach data into text
import smtplib # pip install secure-smtplib == send email
import wikipedia # pip install wikipedia == search wikipedia
import webbrowser # pip install webbrowser == open browser
import os # pip install os == open file
# import pyautogui # pip install pyautogui == take screenshot
# import psutil # pip install psutil == get battery percentage
# import pyjokes # pip install pyjokes == get jokes

# from secrets import sender_email, sender_password, To # pip install python-dotenv == hide email and password
engine = pyttsx3.init()

# ********************* Speak Function ***********************
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# ********************* Vocie Change Function ***********************
def getvoices(voice):
    voices = engine.getProperty('voices')
    # print(voices[1].id)
    if voice == 1:
        engine.setProperty('voice', voices[0].id)
        # speak("Hello sir to select my voice press 1")
    if voice == 2:
        engine.setProperty('voice', voices[1].id)
        # speak("Hello sir to select my voice press 2")

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
        r.pause_threshold = 1 # 1 second pause to indicate end of speaking
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print(f"User Said: {query}\n")

    except Exception as e:
        print(e)
        speak("Say that again please...")

        return "None"
    return query

#*********************** Quit Function ***********************
def quit():
    speak("Thanks for using me sir, have a good day.")
    exit()

# ********************* Send Email Function ***********************
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, to, content)
    server.close()


# ********************* Main Function ***********************
if __name__ == "__main__":
    getvoices(1)
    wishme()

    # ********** Logic for executing tasks based on query ***********
    while True:
       
        query = takeCommandMic().lower() # convert query into lower case so we don't get error in if condition when we say "Open Youtube" instead of "open youtube" or "OPEN YOUTUBE" etc.
       
        # *********** time ***********
        if 'time' in query:
            time()

        # *********** date ***********
        elif 'date' in query:
            date()
        
        # *********** wikipedia ***********
        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")  # replace wikipedia with nothing in the query string so we don't get error in wikipedia search process when searching for something like "wikipedia time"
            results = wikipedia.summary(query, sentences=2) # Wikipedia will give the summary in 2 sentences of the query  # pip install wikipedia
            speak("According to Wikipedia")
            print(results)
            speak(results)

        # *********** Open Youtube ***********
        elif 'open youtube' in query:
            speak("Opening Youtube...")
            webbrowser.open("youtube.com")

        # *********** Open Google ***********
        elif 'open google' in query:
            speak("Opening Google...")
            webbrowser.open("google.com")
        
        # *********** Open Stackoverflow ***********
        elif 'open stackoverflow' in query:
            speak("Opening Stackoverflow...")
            webbrowser.open("stackoverflow.com")
        
        # *********** Open Github ***********
        elif 'open github' in query:
            speak("Opening Github...")
            webbrowser.open("github.com")

        # *********** Open Facebook ***********
        elif 'open facebook' in query:
            speak("Opening Facebook...")
            webbrowser.open("facebook.com")
        
        # *********** Open Instagram ***********
        elif 'open instagram' in query:
            speak("Opening Instagram")
            webbrowser.open("instagram.com")

        # *********** Open Classroom ***********
        elif 'Classroom' in query:
            speak("opening Classroom")
            webbrowser.open("classroom.google.com")

        # *********** Play music ***********
        elif 'play music' in query:
            music_dir = 'D:\Songs\Hanuman ji'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        # *********** Open vs code workspace ***********
        elif 'Python workspace' in query:
            VsCodePath = "C:\\Users\\khand\\OneDrive\\Desktop\\Python-Copy.code-workspace"
            os.startfile(VsCodePath)

        # *********** Remember ***********
        elif 'remember that' in query:
            speak("What should i remember?")
            data = takeCommandMic()
            speak("You said me to remember that" + data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()

        # *********** Volume ***********
        elif 'volume' in query:
            speak("Sir, please tell me the volume level you want to set")
            volume = takeCommandMic()
            engine.setProperty('volume', volume)
            speak(f"Sir, I have set the volume to {volume}")

        # *********** Send Email ***********
        elif 'send email' in query:
            try:
                speak("What should i say?")
                content = takeCommandMic()
                to = To
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Unable to send the email")
        

        # *********** Exit ***********
        elif 'exit' in query:
            quit()
            


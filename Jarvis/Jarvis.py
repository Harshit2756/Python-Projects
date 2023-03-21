import pyttsx3  # pip install pyttsx3  == text data into speech
import datetime  # pip install datetime == get date and time
# pip install speechRecognition == speech data into text
import speech_recognition as sr
import smtplib  # pip install secure-smtplib == send email
# pip install email == send email with attachment
from email.message import EmailMessage
import wikipedia  # pip install wikipedia == search wikipedia
import webbrowser  # pip install webbrowser == open browser
from time import sleep  # pip install time == sleep function to wait for some time
import os  # pip install os == open file
# pip install pywhatkit == to play video on youtube and send message on whatsapp grp
import pywhatkit
from newsapi import NewsApiClient
import pyautogui  # pip install pyautogui == to auto press keyboard
import clipboard

# import psutil # pip install psutil == get battery percentage
# import pyjokes # pip install pyjokes == get jokes

# pip install python-dotenv == hide email and password
from secrets import sender_email, sender_password, To
engine = pyttsx3.init()

# ********************* Speak Function ***********************
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# ********************* Voice Change Function ***********************
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


# ~ ************ Take Command Through CMD Function *************
def takeCommandCMD():
    query = input("Command: ")
    return query


# ~ ************ Take Command Through Mic Function *************
def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # 1 second pause to indicate end of speaking
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


# ! ********************* Send Email Function ***********************
def sendEmail(To, Subject, content):
    # 587 is port number for gmail server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(sender_email, sender_password)
    Email = EmailMessage()
    Email['From'] = sender_email
    Email['To'] = To
    Email['Subject'] = Subject
    Email.set_content(content)
    server.send_message(Email)
    server.close()


# ********************* Send Whatsapp Message Function ***********************
def sendwhatsappmsg(phone_no, message):
    Message = message
    webbrowser.open("https://web.whatsapp.com/send?phone=+91" +
                    phone_no + "&text=" + Message)
    #!use pywhatkit instead to send the message/images to the grp  refer :https://pypi.org/project/pywhatkit/
    sleep(10)
    pyautogui.press('enter')


# ********************* search google ***********************
def searchgoogle():
    speak('Whats should i search for?')
    search = takeCommandMic()
    webbrowser.open('https://www.google.com/search?q=' + search)


# ***************** News update ****************
def news():
    newsapi = NewsApiClient(api_key='5f5422d5735d45d2a17b21db6ed5859a')
    speak('what topic you need the news on?')
    topic = takeCommandMic()
    data = newsapi.get_top_headlines(q='topic',
                                     language='en',
                                     page_size=5)

    newsdata = data['articles']
    for x, y in enumerate(newsdata):
        print(f'{x},{y["description"]}')
        speak(f'{x},{y["description"]}')

    speak("that's all for now ")


# *********** Text to speech ***********
def text_to_speech():
    text = clipboard.paste()
    speak(text)
    print(text)


# ********************* Take Screenshot Function ***********************
# def screenshot():
#     img = pyautogui.screenshot()
#     img.save("C:\\Users\\Harsh\\Desktop\\Jarvis\\screenshot.png")

    # *********************** Quit Function ***********************


def quit():
    speak("Thanks for using me sir, have a good day.")
    exit()


# ********************* Main Function ***********************
if __name__ == "__main__":
    getvoices(1)
    # wishme()

    # ********** Logic for executing tasks based on query ***********
    while True:

        # convert query into lower case so we don't get error in if condition when we say "Open Youtube" instead of "open youtube" or "OPEN YOUTUBE" etc.
        query = takeCommandMic().lower()

        # /******* time ***********
        if 'time' in query:
            time()

        # *********** date ***********
        elif 'date' in query:
            date()

        # *********** wikipedia ***********
        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            # replace wikipedia with nothing in the query string so we don't get error in wikipedia search process when searching for something like "wikipedia time"
            query = query.replace("wikipedia", "")
            # Wikipedia will give the summary in 2 sentences of the query  # pip install wikipedia
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        # ********** google ***********
        elif 'search google' in query:
            searchgoogle()

        # *********** Open Youtube ***********
        elif 'open youtube' in query:
            speak("Opening Youtube...")
            webbrowser.open("youtube.com")

        # ************* youtube search ********
        elif 'search youtube' in query:
            speak("what should i search on youtube?")
            topic = takeCommandMic()
            pywhatkit.playonyt(topic)

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

        # ! *********** Send Email ***********
        elif 'mail' in query:
            email_list = {'harshit': 'harshit.khandelwal20@pccoepune.org'}
            try:
                speak("To Whom you want to send email?")
                To = email_list[takeCommandMic().lower()]
                speak("What should be the subject of email?")
                Subject = takeCommandMic()

                speak("What should i say?")
                content = takeCommandMic()

                sendEmail(To, Subject, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Unable to send the email")

        # *********** Send Whatsapp Message ***********
        elif 'whatsapp' in query:
            user_name = {
                'Siddhi': '+91 70200 58417'
            }
            try:
                speak("To whom you want to send whatsapp message?")
                phone_no = user_name[takeCommandMic().lower()]

                speak("What should i say?")
                message = takeCommandMic()

                sendwhatsappmsg(phone_no, message)
                speak("Message has been sent!")

            except Exception as e:
                print(e)
                speak("Unable to send the message")

        # ! *********** wheather **********
        elif 'wheather' in query:
            wether = query['wheather']

        # *********** News **************
        elif 'news' in query:
            news()

        # *********** Text to speech ********
        elif 'read' in query:
            text_to_speech()

        # ********** Mail
        # # *********** Take Screenshot ***********
        # elif 'screenshot' in query:
        #     speak("Taking screenshot...")
        #     screenshot()
        #     speak("Screenshot has been taken!")

        # *********** Exit ***********
        elif 'exit' in query:
            quit()

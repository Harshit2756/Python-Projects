import ctypes
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
import pyjokes  # pip install pyjokes == get jokes
import string
import random  # pip install random == generate random password
import psutil  # pip install psutil == get battery percentage
from nltk.tokenize import word_tokenize # pip install nltk == tokenization of words in a sentence 
# ! pip install python-dotenv == hide email and password

from secrets import sender_email, sender_password, To

from newvoices import speak

engine = pyttsx3.init()
"""

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
"""

# ********************* Time Function ***********************
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)


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


# ********************* Date Function ***********************
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)


# ********************* Wishme Function ***********************
def wishme():
    speak("Welcome back sir!")
    greeting()
    speak("Jarvis at your service. Please tell me how can i help you?")


# ************ Take Command Through CMD Function *************
def takeCommandCMD(info):
    query = pyautogui.prompt(text=f'Enter {info}', title='Jarvis', default='')
    return query


# ************ Take Command Through Mic Function *************
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


# ~ ********************* Send Whatsapp Message Function ***********************
def sendwhatsappmsg(phone_no, message):
    Message = message
    webbrowser.open("https://web.whatsapp.com/send?phone=+91" +
                    phone_no + "&text=" + Message)
    #!use pywhatkit instead to send the message/images to the grp  refer :https://pypi.org/project/pywhatkit/
    sleep(10)
    pyautogui.press('enter')


# ********************* search google ***********************
def search_google():
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
def screenshot():
    speak("What name should i save the screenshot")
    img_name = takeCommandMic()
    img_name = 'C:\\Users\\khand\\OneDrive\\Pictures\\Screenshots\\{}.png'.format(
        img_name)
    img = pyautogui.screenshot(img_name)
    img.show()

# ********************* Generate Password Function *********************
def generate_password():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    speak("Please enter the password length")
    text = "password length"
    passlen = int(takeCommandCMD(text))
    password = []
    password.extend(list(s1))
    password.extend(list(s2))
    password.extend(list(s3))
    password.extend(list(s4))

    random.shuffle(password)
    password = ("".join(password[0:passlen]))
    speak("Your password is"+password)
    print(password)


# ********************* Find location ***********************
def find_location():
    speak("What is the location?")
    location = takeCommandMic()
    url = 'https://google.nl/maps/place/' + location + '/&amp;'
    webbrowser.get().open(url)
    speak("Here is the location of " + location)
    pyautogui.click(x=394, y=159)


# ********************* Flip a coin ***********************
def flip_coin():
    print("flipping a coin...")
    speak("flipping a coin")
    coin = ['head', 'tail']
    speak('I fliped the coin '+random.choice(coin))


# ********************* Roll a dice ***********************
def roll_dice():
    print("rolling a dice...")
    dice = ['1', '2', '3', '4', '5', '6']
    speak("rolling a dice")
    speak('i rolled the dice you got '+random.choice(dice))


# ********************* cpu usage ***********************
def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage)


# ********************* battery ***********************
def battery():
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)


# *********************** Quit Function ***********************
def quit():
    speak("Thanks for using me sir, have a good day.")
    exit()


# / ********************* Main Function ***********************
if __name__ == "__main__":
    wishme()

    # ********** Logic for executing tasks based on query ***********
    while True:

        # convert query into lower case so we don't get error in if condition when we say "Open Youtube" instead of "open youtube" or "OPEN YOUTUBE" etc.
        query = takeCommandMic().lower()
        query = word_tokenize(query)
        print (query)

        wake_word="jarvis"

        if wake_word in query:

            # ******* time ***********
            if 'time' in query:
                try:
                    time()
                except Exception as e:
                    print(e)
                    speak("Sorry, I am not able to find that")

            # *********** date ***********
            elif 'date' in query:
                try:
                    date()
                except Exception as e:
                    print(e)
                    speak("Sorry, I am not able to find that")

            # *********** wikipedia ***********
            elif 'wikipedia' in query:
                try:
                    speak("Searching Wikipedia...")
                    # replace wikipedia with nothing in the query string so we don't get error in wikipedia search process when searching for something like "wikipedia time"
                    query = query.replace("wikipedia", "")
                    # Wikipedia will give the summary in 2 sentences of the query  # pip install wikipedia
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                except Exception as e:
                    print(e)
                    speak("Sorry, I am not able to find that")

            # ********** google ***********
            elif 'search google' in query:
                try:
                    search_google()
                except Exception as e:
                    print(e)
                    speak("Sorry, I am not able to find that")

            # *********** Open Youtube ***********
            elif 'open youtube' in query:
                try:
                    speak("Opening Youtube...")
                    webbrowser.open("youtube.com")
                except Exception as e:
                    print(e)
                    speak("Sorry, I am not able to find that")

            # ************* youtube search ********
            elif 'search youtube' in query:
                try:
                    speak("what should i search on youtube?")
                    topic = takeCommandMic()
                    pywhatkit.playonyt(topic)
                except Exception as e:
                    print(e)
                    speak("Sorry, I am not able to find that")

            # *********** Open Google ***********
            elif 'open google' in query:
                try:
                    speak("Opening Google...")
                    webbrowser.open("google.com")
                except Exception as e:
                    print(e)
                    speak("Sorry, I am not able to do that")

            # *********** Open Stackoverflow ***********
            elif 'open stackoverflow' in query:
                try:
                    speak("Opening Stackoverflow...")
                    webbrowser.open("stackoverflow.com")
                except Exception as e:
                    print(e)
                    speak("Sorry, I am not able to find that")

            # *********** Open Github ***********
            elif 'open github' in query:
                try:
                    speak("Opening Github...")
                    webbrowser.open("github.com")
                except Exception as e:
                    print(e)
                    speak("Sorry, I am not able to find that")

            # *********** Open Facebook ***********
            elif 'open facebook' in query:
                try:
                    speak("Opening Facebook...")
                    webbrowser.open("facebook.com")
                except Exception as e:
                    print(e)
                    speak("Sorry, I am not able to find that")

            # *********** Open Instagram ***********
            elif 'open instagram' in query:
                try:
                    speak("Opening Instagram")
                    webbrowser.open("instagram.com")
                except Exception as e:
                    print(e)
                    speak("Sorry, I am not able to do that")

            # *********** Open Classroom ***********
            elif 'Classroom' in query:
                try:
                    speak("Opening Classroom")
                    webbrowser.open("classroom.google.com")
                except Exception as e:
                    print(e)
                    speak("Sorry, I am not able to do that")

            # *********** Play music ***********
            elif 'play music' in query:
                try:
                    music_dir = 'D:\Songs\Hanuman ji'
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[0]))
                except Exception as e:
                    print(e)
                    speak("Sorry, I am not able to play music")

            # *********** Remember ***********
            elif 'remember that' in query:
                try:
                    speak("What should i remember?")
                    data = takeCommandMic()
                    speak("You said me to remember that" + data)
                    remember = open('data.txt', 'w')
                    remember.write(data)
                    remember.close()
                except Exception as e:
                    print(e)
                    speak("Sorry, I am not able to remember that")

            # *********** Do you remember ***********
            elif 'do you remember anything' in query:
                try:
                    remember = open('data.txt', 'r')
                    speak("You said me to remember that" + remember.read())
                except Exception as e:
                    print(e)
                    speak("Sorry, I am not able to remember that")

            # *********** Volume ***********
            elif 'volume' in query:
                try:
                    speak("Sir, please tell me the volume level you want to set")
                    volume = takeCommandMic()
                    engine.setProperty('volume', volume)
                    speak(f"Sir, I have set the volume to {volume}")
                except Exception as e:
                    print(e)
                    speak("Sorry, I am not able to set the volume")

            # ! *********** Send Email ***********
            elif 'send mail' in query:
                email_list = {'harshit': 'harshit.khandelwal20@pccoepune.org'}
                for email in email_list:
                    print(email)

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
                for user in user_name:
                    print(
                        user
                    )
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
                try:
                    news()
                except Exception as e:
                    print(e)
                    speak("Sorry, I am not able to find that")

            # *********** Text to speech ********
            elif 'read' in query:
                try:
                    text_to_speech()
                except Exception as e:
                    print(e)
                    speak("Sorry, I am not able to find that")

            # ************ rambox *************
            elif 'rambox' in query:
                try:
                    rambox = "C:\\Program Files\\Rambox\\Rambox.exe"
                    os.startfile(rambox)
                except Exception as e:
                    print(e)
                    speak("Sorry, I am not able to find that")

            # *********** Open vs code workspace ***********
            elif 'Python workspace' in query:
                try:
                    VsCodePath = "C:\\Users\\khand\\OneDrive\\Desktop\\Python-Copy.code-workspace"
                    os.startfile(VsCodePath)
                except Exception as e:
                    print(e)
                    speak("Sorry, I am not able to find that")

            # ! ************ c drive *************
            elif 'open' in query:
                os.startfile('explorer C://{}'.format(query.replace('open', '')))

            # ********** joke *************
            elif 'joke' in query:
                try:
                    print(pyjokes.get_joke())
                    speak(pyjokes.get_joke())
                except Exception as e:
                    print(e)
                    speak("Sorry, I am not able to find that")

            # ************ password ********
            elif 'password' in query:
                try:
                    generate_password()
                except Exception as e:
                    print(e)
                    speak("Sorry, I am not able to generate the password")

            # *********** flip a coin ***********
            elif 'flip a coin' in query:
                try:
                    flip_coin()
                except Exception as e:
                    print(e)
                    speak("Sorry, I am not able to flip the coin")

            # *********** roll a dice ***********
            elif 'roll a dice' in query:
                try:
                    roll_dice()
                except Exception as e:
                    print(e)
                    speak("Sorry, I am not able to roll the dice")

            # *********** find location ***********
            elif 'location' in query:
                try:
                    find_location()
                except Exception as e:
                    print(e)
                    speak("Sorry, I am not able to find the location")

            # *********** Take Screenshot ***********
            elif 'screenshot' in query:
                try:
                    speak("Taking screenshot...")
                    screenshot()
                    speak("Screenshot has been taken!")
                except Exception as e:
                    print(e)
                    speak("Sorry, I am not able to do that")

            # *********** Battery CPU ***********
            elif 'battery' in query:
                try:
                    battery()
                except Exception as e:
                    print(e)
                    speak("Sorry, I am not able to do that")

            # *********** CPU ***********
            elif 'cpu' in query:
                try:
                    cpu()
                except Exception as e:
                    print(e)
                    speak("Sorry, I am not able to do that")

            # *********** Exit ***********
            elif 'exit' in query:
                try:
                    quit()
                except Exception as e:
                    print(e)
                    speak("Sorry, I am not able to do that")

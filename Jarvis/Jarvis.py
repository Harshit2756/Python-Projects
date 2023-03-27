import ctypes  # pip install ctypes == to system call
import pytube  # pip install pytube == download youtube video
import pyttsx3  # pip install pyttsx3  == text data into speech
import datetime  # pip install datetime == get date and time
# pip install speechRecognition == speech data into text
import speech_recognition as sr
import smtplib  # pip install secure-smtplib == send email
# pip install email == send email with attachment
import wikipedia  # pip install wikipedia == search wikipedia
import webbrowser  # pip install webbrowser == open browser
import os  # pip install os == open file
# pip install pywhatkit == to play video on youtube and send message on whatsapp grp
import pywhatkit
import pyautogui  # pip install pyautogui == to auto press keyboard
import clipboard
import pyjokes  # pip install pyjokes == get jokes
import string
import speedtest  # pip install speedtest-cli == get internet speed
import random  # pip install random == generate random password
import psutil  # pip install psutil == get battery percentage
from requests import get  # pip install requests == to get ip address
from email.message import EmailMessage
from time import sleep  # pip install time == sleep function to wait for some time
from newsapi import NewsApiClient
# pip install nltk == tokenization of words in a sentence
from nltk.tokenize import word_tokenize
# ! pip install python-dotenv == hide email and password

from secrets import sender_email, sender_password, To

# from newvoices import speak

engine = pyttsx3.init()


# ********************* Speak Function ***********************
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# ********************* Voice Change Function ***********************
def change_voice():
    voices = engine.getProperty('voices')
    if voices == 0:
        engine.setProperty('voice', voices[1].id)
    if voices == 1:
        engine.setProperty('voice', voices[0].id)

    speak("Hello sir ,I have successfully changed my voice")


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
    query = pyautogui.prompt(text=f'{info}', title='Jarvis', default='')
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


#  ********************* Send Email Function ***********************
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
def sendwhatsappmsg(to):
    #! use pywhatkit instead to send the message/images to the grp  refer :https://pypi.org/project/pywhatkit/

    user_name = {'harshit': '+91 63536 59331', 'pranam': '+91 70415 87406',
                 'adu padu': '+91 93257 61961', 'gayatri kulkarni': '+91 80104 49116'}
    grp_name = {'me', 'itsa', 'error 202'}
    if to in user_name:
        to = user_name[to]
        speak("What should i say?")
        message = takeCommandMic()
        pywhatkit.sendwhatmsg_instantly(f'{to}', f"{message}")
    elif to in grp_name:
        to = grp_name[to]
        speak("What should i say?")
        message = takeCommandMic()
        pywhatkit.sendwhatmsg_to_group_instantly(f'{to}', f"{message}")
    else:
        speak("I don't have the contact in my database")

# ********************* Send Whatsapp Image Function ***********************
def sendwhatsappimg(to, message):
    user_name = {'harshit': '+91 63536 59331', 'pranam': '+91 70415 87406',
                 'adu padu': '+91 93257 61961', 'gayatri kulkarni': '+91 80104 49116'}
    grp_name = {'me', 'itsa', 'error 202'}
    if to in user_name:
        to = user_name[to]

        speak("What should i say?")
        message = takeCommandMic()

        speak("What is the path of the image?")
        image_path = takeCommandCMD("Enter the path of the image:")

        pywhatkit.sendwhats_image(f"{to}", f"{image_path}", f"{message}")
    elif to in grp_name:
        to = grp_name[to]

        speak("What should i say?")
        message = takeCommandMic()

        speak("What is the path of the image?")
        image_path = takeCommandCMD("Enter the path of the image:")

        pywhatkit.sendwhats_to_group(f"{to}", f"{image_path}", f"{message}")
    else:
        speak("I don't have the contact in my database")


# ***************** News update ****************
def news():
    newsapi = NewsApiClient(api_key='5f5422d5735d45d2a17b21db6ed5859a')
    speak('what topic you need the news on?')
    topic = takeCommandMic()
    data = newsapi.get_top_headlines(q='topic',
                                     language='en',
                                     page_size=5)

    newsdata = data['articles']
    for index, y in enumerate(newsdata):
        print(f'{index},{y["description"]}')
        speak(f'{index},{y["description"]}')

    speak("that's all for now ")
    speak("Do you want to hear more news?") 
    ans = takeCommandMic()
    if 'yes' in ans:
        news() 


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


# ********************* Open Application Function ***********************
def open_application(query):
    try:
        # ********** camera **********
        if "camera" in query:
            speak("Opening camera")
            print("Opening camera ...")
            os.system("start microsoft.windows.camera:")
        # ********** cmd **********
        elif ("cmd" in query) or ("cammond prompt" in query):
            speak("Opening cmd")
            print("Opening cmd ...")
            os.system("start cmd")
        # ********** notepad **********
        elif "notepad" in query:
            speak("Opening notepad")
            print("Opening notepad ...")
            os.system("start notepad")
        # ********** paint **********
        elif "paint" in query:
            speak("Opening paint")
            print("Opening paint ...")
            os.system("start mspaint")
        # ********** calculator **********
        elif "calculator" in query:
            speak("Opening calculator")
            print("Opening calculator ...")
            os.system("start calculator")
        # ********** control panel **********
        elif "control panel" in query:
            speak("Opening control panel")
            print("Opening control panel ...")
            os.system("start control")
        # ********** task manager **********
        elif "task manager" in query:
            speak("Opening task manager")
            print("Opening task manager ...")
            os.system("start taskmgr")
        # ********** file explorer **********
        elif "file explorer" in query:
            speak("Opening file explorer")
            print("Opening file explorer ...")
            os.system("start explorer")
        # ********** one note **********
        elif "one note" in query:
            speak("Opening one note")
            print("Opening one note ...")
            os.system("start onenote")
        # ********** power point **********
        elif "power point" in query:
            speak("Opening power point")
            print("Opening power point ...")
            os.system("start powerpnt")
        # ********** word **********
        elif "word" in query:
            speak("Opening word")
            print("Opening word ...")
            os.system("start winword")
        # ********** excel **********
        elif "excel" in query:
            speak("Opening excel")
            print("Opening excel ...")
            os.system("start excel")
        # ********** notion **********
        elif "notion" in query:
            speak("Opening notion")
            print("Opening notion ...")
            rambox = "C:\\Program Files\\Rambox\\Rambox.exe"
            os.startfile(rambox)
        # ********** rambox **********
        elif "rambox" in query:
            speak("Opening rambox")
            print("Opening rambox ...")
            notion = "C:\Users\\khand\\AppData\\Local\\Programs\\Notion\\Notion.exe"
            os.startfile(notion)
        # ********** primevideo **********
        elif "primevideo" in query:
            speak("Opening primevideo")
            print("Opening primevideo ...")
            primevideo = primevideo = "C:\\Program Files\\WindowsApps\\AmazonVideo.PrimeVideo_1.0.116.0_x64__pwbj9vvecjh7j\\PrimeVideo.exe"
            os.startfile(primevideo)
        # ********** telegram **********
        elif "telegram" in query:
            speak("Opening telegram")
            print("Opening telegram ...")
            telegram = "C:\\Program Files\\WindowsApps\\TelegramMessengerLLP.TelegramDesktop_4.6.3.0_x64__t4vj0pshhgkwm\\Telegram.exe"
            os.startfile(telegram)
        # ********** python workspace **********
        elif "python workspace" in query:
            speak("Opening python workspace")
            print("Opening python workspace ...")
            python_workspace = "C:\\Users\\khand\\OneDrive\\Desktop\\Python-Copy.code-workspace"
            os.startfile(python_workspace)
    except Exception as e:
        print(e)
        speak("Sorry, I am not able to find that")

# todo: if the below logic work concise all the other things like open google, open youtube etc.
open = {'open camera', 'open cmd', 'open cammond prompt', 'open notepad', 'open paint', 'open calculator', 'open control panel', 'open control panel', 'open task manager', 'open file explorer','open one note', 'open power point', 'open word', 'open excel', 'open notion','open rambox','open primevideo','open telegram','open python workstation'}
quit = {'quit', 'exit', 'bye', 'goodbye', 'see you later', 'see you soon', 'see you','good night', 'goodbye jarvis', 'good night jarvis', 'good bye', 'good night sir'}

# / ********************* Main Function ***********************
if __name__ == "__main__":
    wishme()

    # ********** Logic for executing tasks based on query ***********
    while True:

        # convert query into lower case so we don't get error in if condition when we say "Open Youtube" instead of "open youtube" or "OPEN YOUTUBE" etc.

        print(query)
        query = query.lower()

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

        # *********** change voice ***********
        elif 'change voice' in query:
            try:
                speak("Changing voice")
                print("Changing voice ...")
                change_voice()
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to do that")

        # . *********** open camera ***********
        elif 'open camera' in query:
            open_application(query)

        # . *********** open cmd ***********
        elif 'open cmd' in query:
            open_application(query)

        # . *********** open notepad ***********
        elif 'open notepad' in query:
            open_application(query)

        # . *********** open paint ***********
        elif 'open paint' in query:
            open_application(query)

        # . *********** open calculator ***********
        elif 'open calculator' in query:
            open_application(query)

        # . *********** open control panel ***********
        elif 'open control panel' in query:
            open_application(query)

        # . *********** open task manager ***********
        elif 'open task manager' in query:
           open_application(query)

        # . *********** open file explorer ***********
        elif 'open file explorer' in query:
            open_application(query)

        # . *********** open onenote ***********
        elif 'open onenote' in query:
            open_application(query)

        # . *********** open powerpoint ***********
        elif 'open powerpoint' in query:
            open_application(query)

        # . *********** open word ***********
        elif 'open word' in query:
            open_application(query)

        # . *********** open excel ***********
        elif 'open excel' in query:
            open_application(query)

        # . ************ rambox *************
        elif 'rambox' in query:
            open_application(query)

        # . ************ notion *************
        elif 'notion' in query:
            open_application(query)

        # . ************ Prime video *************
        elif 'prime video' in query:
            open_application(query)

        # . ************ Telegram *************
        elif 'telegram' in query:
            open_application(query)

        # . *********** Open vs code workspace ***********
        elif 'Python workspace' in query:
            open_application(query)

        # ~ *********** Text to speech ********
        elif 'read' in query:
            try:
                text_to_speech()
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to find that")

        # ~ *********** Take Screenshot ***********
        elif 'screenshot' in query:
            try:
                speak("Taking screenshot...")
                screenshot()
                speak("Screenshot has been taken!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to do that")

        # ~ *********** Battery CPU ***********
        elif 'battery' in query:
            try:
                battery = psutil.sensors_battery()
                speak("Battery is at")
                speak(battery.percent)
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to do that")

        # ~ *********** CPU ***********
        elif 'cpu' in query:
            try:
                usage = str(psutil.cpu_percent())
                speak("CPU is at"+usage)
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to do that")

        # ~ *********** volume ***********
        elif 'volume' in query:
            if ('volume up' in query) or ('increase volume' in query):
                try:
                    pyautogui.press("volumeup")
                    speak("Volume increased")
                except Exception as e:
                    print(e)
                    speak("Sorry, I am not able to do that")
            elif ('volume down' in query) or ('decrease volume' in query):
                try:
                    pyautogui.press("volumedown")
                    speak("Volume decreased")
                except Exception as e:
                    print(e)
                    speak("Sorry, I am not able to do that")
            elif ('mute volume' in query) or ('mute' in query):
                try:
                    pyautogui.press("volumemute")
                    speak("Volume muted")
                except Exception as e:
                    print(e)
                    speak("Sorry, I am not able to do that")

        # ~ *********** jarvis volume ***********
        elif 'your volume' in query:
            try:
                speak("Sir, please tell me the volume level you want to set for me")
                volume = takeCommandMic()
                engine.setProperty('volume', volume)
                speak(f"Sir, I have set the volume to {volume}")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to set the volume")

        # ~ *********** shutdown ***********
        elif 'shutdown' in query:
            try:
                speak("Shutting down the system in 3 seconds")
                # shutdown , /s = shutdown, /r = restart, /l = log off, /h = hibernate, / ki jaga - use kar sakte hai
                os.system("shutdown /s /t 3")   # shutdown , /s = shutdown, /t = time, 3 =after 3 sec system will shutdown
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to do that")

        # ~ *********** restart ***********
        elif 'restart' in query:
            try:
                speak("Restarting the system in 3 seconds")
                os.system("shutdown /r /t 1") # restart , /r = restart, /t = time, 3 =after 3 sec system will restart
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to do that")

        # ~ *********** logout ***********
        elif 'logout' in query:
            try:
                speak("Logging out the system")
                os.system("shutdown -l")  # logout , -l = logout 
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to do that")

        # ~ *********** hibernate ***********
        elif 'hibernate' in query:
            try:
                speak("Hibernating the system")
                os.system("shutdown /h")    # hibernate , /h = hibernate
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to do that")

        # ~ *********** sleep ***********
        elif 'sleep' in query:
            try:
                speak("Sleeping the system")
                # - sleep , rundless32.exe = run dll, powrprof.dll = power profile, SetSuspendState = set suspend state, 0,1,0 = 0 = sleep, 1 = hibernate, 0 = no force
                # - The command you provided is used to put the computer into sleep mode. The rundll32.exe program is used to run DLL files as if they were programs. In this case, it’s being used to run the powrprof.dll file, which contains functions related to power management. The SetSuspendState function is used to set the suspend state of the system. The 0,1,0 parameter tells the function to put the system into sleep mode, and not hibernate mode. The 0 parameter tells the function to not force the system to sleep, but to allow the system to decide whether it can sleep or not.
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0") 
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to do that")

        # ~ *********** lock ***********
        elif 'lock' in query:
            try:
                speak("Locking the system")
                ctypes.windll.user32.LockWorkStation() # lock , LockWorkStation is a function in user32.dll that locks the workstation
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to do that")

        # ~ *********** change wallpaper ***********
        elif 'change wallpaper' in query:
            try:
                speak("Changing wallpaper")
                speak("What is the path of the wallpaper?")
                wallpaper_path = takeCommandCMD(
                    "Enter the path of the wallpaper:")
                ctypes.windll.user32.SystemParametersInfoW(
                    20, 0, wallpaper_path, 0)  # change wallpaper , SystemParametersInfoW is a function in user32.dll that changes the system parameters of the system , 20 = SPI_SETDESKWALLPAPER, 0 = the change should be applied immediately , wallpaper_path = path of the wallpaper, 0 = that the change should apply to all users.
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to do that")

        # *********** internet speed ***********
        elif 'internet speed' in query:
            try:
                speak("Checking internet speed")
                st = speedtest.Speedtest()
                down = st.download()
                up = st.upload()
                speak(f"Download speed is {down}")
                speak(f"Upload speed is {up}")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to do that")

        # *********** ip address ***********
        elif 'ip address' in query:
            try:
                ip = get('https://api.ipify.org').text
                speak(f"Your IP address is {ip}")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to do that")

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

        # *********** Open Google ***********
        elif 'open google' in query:
            try:
                speak("Opening Google...")
                webbrowser.open("google.com")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to do that")
        
        # *********** search google ***********
        elif 'search google' in query:
            try:
                speak("What do you want to search on Google?")
                search_term = takeCommandMic().replace(
                    "search", "").replace("google", "").strip()
                search_term = search_term.replace(
                    "for", "").strip().replace(" ", "+")
                webbrowser.open(
                    f'https://www.google.com/search?q={search_term}')
                speak(f"Here are the results for {search_term} on Google")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to do that")
        
        # *********** Open Youtube ***********
        elif 'open youtube' in query:
            try:
                speak("Opening Youtube...")
                webbrowser.open("youtube.com")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to find that")

        #  *********** search youtube ***********
        elif 'search youtube' in query:
            try:
                speak("What do you want to search on YouTube?")
                search_term = takeCommandMic().replace(
                    "search", "").replace("YouTube", "").strip()
                search_term = search_term.replace(
                    "for", "").strip().replace(" ", "+")
                webbrowser.open(f'https://www.youtube.com/results?search_query={search_term}')
                speak(f"Here are the results for {search_term} on YouTube")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to do that")

        # *********** play music on youtube ***********
        elif ('play music on youtube' in query) or ('search music on youtube' in query) or ('search youtube' in query):
            try:
                speak("What do you want to listen on YouTube?")
                search_term = takeCommandMic().replace("play", "").replace("music", "").strip()
                search_term = search_term.replace(
                    "on", "").strip().replace(" ", "+")
                webbrowser.open(
                    f'https://www.youtube.com/results?search_query={search_term}')
                speak(f"Here are the results for {search_term} on YouTube")
                speak("Which one do you want to play?")
                search_result = takeCommandMic().lower()
                if "first" in search_result:
                    pyautogui.moveTo(x=416, y=195, duration=2)
                    pyautogui.click(button='left')
                    speak("Playing the first result on YouTube")
                elif "second" in search_result:
                    pyautogui.moveTo(x=416, y=250, duration=2)
                    pyautogui.click(button='left')
                    speak("Playing the second result on YouTube")
                elif "third" in search_result:
                    pyautogui.moveTo(x=416, y=320, duration=2)
                    pyautogui.click(button='left')
                    speak("Playing the third result on YouTube")
                else:
                    speak("Sorry, I am not able to do that")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to do that")

        # ! *********** youtube download ***********
        elif 'download youtube' in query:
            try:
                speak("Sir please enter the link of the video")
                link = takeCommandCMD("Enter the link of the video:")
                speak("Sir please enter the path where you want to save the video")
                path = takeCommandCMD(
                    "Enter the path where you want to save the video:")
                speak("Sir please enter the name of the video")
                name = takeCommandCMD("Enter the name of the video:")
                speak("Downloading the video")
                pytube.YouTube(link).streams.first().download(path, name)
                speak("Video downloaded")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to find that")

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

        # *********** Open Gmail ***********
        elif 'open gmail' in query:
            try:
                speak("Opening Gmail...")
                webbrowser.open("gmail.com")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to find that")

        # *********** Play music ***********
        elif 'play music' in query:
            try:
                music_dir = 'D:\Songs\Hanuman ji'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to play music")

        # *********** find location ***********
        elif 'location' in query:
            try:
                speak("What is the location?")
                location = takeCommandMic()
                speak("Hold on, I will show you " +
                      location + "on google maps")
                url = 'https://google.nl/maps/place/' + location + '/&amp;'
                webbrowser.get().open(url)
                speak("Here is the location of " + location)
                pyautogui.click(x=394, y=159)
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to find the location")

        # ! *********** Send Email ***********
        elif 'send mail' in query:
            try:
                speak("To Whom you want to send email?")
                To = takeCommandCMD("Enter the Email Id ?")

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
            try:
                speak("To whom you want to whatsapp ?")
                to = takeCommandMic().lower()

                speak("what do you want to send ,image or message?")
                type = takeCommandMic().lower()
                if type == "image":
                    speak("To whom you want to send whatsapp image?")
                    to = takeCommandMic().lower()

                    sendwhatsappimg(to)

                    speak("Image has been sent!")
                elif type == "message":
                    sendwhatsappmsg(to)
                    speak("Message has been sent!")
            except Exception as e:
                print(e)
                speak("Unable to send the message")

        # *********** News **************
        elif 'news' in query:
            try:
                news()
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to find that")

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
                print("flipping a coin...")
                speak("flipping a coin")
                coin = ['head', 'tail']
                speak('I fliped the coin '+random.choice(coin))
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to flip the coin")

        # *********** roll a dice ***********
        elif 'roll a dice' in query:
            try:
                print("rolling a dice...")
                dice = ['1', '2', '3', '4', '5', '6']
                speak("rolling a dice")
                speak('i rolled the dice you got '+random.choice(dice))
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to roll the dice")

        # *********** Exit ***********
        elif quit in query:
            try:
                speak("Thanks for using me sir, have a good day.")
                exit()
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to do that")

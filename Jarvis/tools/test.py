from nltk.tokenize import word_tokenize

sentance = "hey jarvis, what is the  in balore?"

words = word_tokenize(sentance)
print(words)


"""
# ********************* youtube download ***********************
def youtube_download():
    speak("What should i download?")
    text = "What should i download?"
    search = takeCommandCMD(text)
    speak("Downloading"+search)
    pywhatkit.playonyt(search)



# ********************* change wallpaper ***********************


def change_wallpaper():
    speak("What wallpaper you want to set?")
    wallpaper = takeCommandMic()
    if 'nature' in wallpaper:
        speak("Ok, setting nature wallpaper")
        ctypes.windll.user32.SystemParametersInfoW(
            20, 0, "C:\\Users\\khand\\OneDrive\\Pictures\\nature.jpg", 0)
    elif 'space' in wallpaper:
        speak("Ok, setting space wallpaper")
        ctypes.windll.user32.SystemParametersInfoW(
            20, 0, "C:\\Users\\khand\\OneDrive\\Pictures\\space.jpg", 0)
    elif 'dark' in wallpaper:
        speak("Ok, setting dark wallpaper")
        ctypes.windll.user32.SystemParametersInfoW(
            20, 0, "C:\\Users\\khand\\OneDrive\\Pictures\\dark.jpg", 0)
    else:
        speak("Sorry, i don't have that wallpaper")



# ! ********************* Play a game ***********************
def play_game():
    speak("Which game you want to play?")
    game = takeCommandMic()
    if 'snake' in game:
        speak("Ok, opening snake game")
        os.startfile(
            'C:\\Users\\khand\\OneDrive\\Desktop\\Jarvis\\snake game\\snake.py')
    elif 'tictactoe' in game:
        speak("Ok, opening tictactoe game")
        os.startfile(
            'C:\\Users\\khand\\OneDrive\\Desktop\\Jarvis\\tictactoe\\tictactoe.py')
    else:
        speak("Sorry, i don't have that game")



# ********************* lock pc ***********************
def lock_pc():
    speak("locking the device")
    ctypes.windll.user32.LockWorkStation()
"""

from nltk.tokenize import word_tokenize

sentance = "hey jarvis, what is the  in balore?"

words = word_tokenize(sentance)
print(words)


"""

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




"""

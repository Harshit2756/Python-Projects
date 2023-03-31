"""
       # ! ~ *********** recording ***********
       elif ("recording" in query) or ("screen recording" in query) or ("voice recording" in query):
            try:
                speak("Sir press q key to stop recordings")
                option = takeCommandMic()
                Record_Option(option=option)
                speak("Sir recording is being saved")
            except:
                speak("Sir an unexpected error occured couldn't start screen recording")

        # ! ~ *********** track a mobile number ***********
        elif ("track" in query) or ("track a mobile number" in query):
            speak("Sir please enter the mobile number with country code")
            try:
                location, servise_prover, lat, lng = Phonenumber_location_tracker()
                speak(
                    f"Sir the mobile number is from {location} and the service provider for the mobile number is {servise_prover}")
                speak(
                    f"latitude of that mobile nuber is {lat} and longitude of that mobile number is {lng}")
                print(location, servise_prover)
                print(f"Latitude : {lat} and Longitude : {lng}")
                speak("Sir location of the mobile number is saved in Maps")
            except:
                speak("Sir an unexpected error occured couldn't track the mobile number")

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

      # ~ *********** open website ***********
        elif 'open' in query and 'website' in query:
            try:
                website_name = query.split("open", 1)[1].split(
                    "website", 1)[0].strip()
                speak(f"Opening {website_name} website")
                if ("http://" not in website_name) and ("https://" not in website_name):
                    website_name = "https://" + website_name
                webbrowser.open(website_name)
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to do that")
        
        # ! *********** timmer ***********
        elif 'timer' in query:
            try:
                speak("For how many minutes?")
                mins = int(takeCommandMic())
                speak("Timer set for " + str(mins) + " minutes")
                time(mins*60)
                speak("Time is up")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to set the timer")

     # *********** tell me a fact ***********
        elif 'tell me a fact' in query:
            try:
                speak("Here is a fact")
                speak(facts.getFact())
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to find that")

    # speak("Do you want news on specific topic?")
    # ans = takeCommandMic().lower()
    # if 'yes' in ans:
    #     newsapi = NewsApiClient(api_key='5f5422d5735d45d2a17b21db6ed5859a')
    #     speak('what\'s topic you need the news on?')
    #     topic = takeCommandMic()
    #     data = newsapi.get_top_headlines(q=topic,
    #                                     language='en',
    #                                     page_size=5)
    #     newsdata = data['articles']
    #     for index, y in enumerate(newsdata):
    #         print(f'{index},{y["description"]}')
    #         speak(f'{index},{y["description"]}')


"""

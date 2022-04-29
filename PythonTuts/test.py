# # import  random
# # number_of_friends=int(input("enter the number of friends\n"))
# # name_list=input(f"enter {number_of_friends} names separated by space\n").split(" ")
# # first_names=[name for name in name_list if name_list.index(name)%2==0 ]
# # last_names= [name for name in name_list if name_list.index(name)%2!=0]
# #
# # for i in range(number_of_friends):
# #     a = random.choice(last_names)
# #     print(f'{first_names[i]} {a}')
# #     last_names.remove(a)
#
#
# # NOTE: this requires PyAudio because it uses the Microphone class
# # import speech_recognition as sr
# # r = sr.Recognizer()
# # sr.Microphone.list_microphone_names()
# # with sr.Microphone() as source:
# #     r.adjust_for_ambient_noise(source)    # use the default microphone as the audio source
# #     audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
# #
# # try:
# #     print("You said " + r.recognize_google(audio))    # recognize speech using Google Speech Recognition
# # except LookupError:                            # speech is unintelligible
# #     print("Could not understand audio")
#
#
# import random
# import time
#
# import speech_recognition as sr
#
#
# def recognize_speech_from_mic(recognizer, microphone):
#     """Transcribe speech from recorded from `microphone`.
#
#     Returns a dictionary with three keys:
#     "success": a boolean indicating whether or not the API request was
#                successful
#     "error":   `None` if no error occured, otherwise a string containing
#                an error message if the API could not be reached or
#                speech was unrecognizable
#     "transcription": `None` if speech could not be transcribed,
#                otherwise a string containing the transcribed text
#     """
#     # check that recognizer and microphone arguments are appropriate type
#     if not isinstance(recognizer, sr.Recognizer):
#         raise TypeError("`recognizer` must be `Recognizer` instance")
#
#     if not isinstance(microphone, sr.Microphone):
#         raise TypeError("`microphone` must be `Microphone` instance")
#
#     # adjust the recognizer sensitivity to ambient noise and record audio
#     # from the microphone
#     with microphone as source:
#         recognizer.adjust_for_ambient_noise(source)
#         audio = recognizer.listen(source)
#
#     # set up the response object
#     response = {
#         "success": True,
#         "error": None,
#         "transcription": None
#     }
#
#     # try recognizing the speech in the recording
#     # if a RequestError or UnknownValueError exception is caught,
#     #     update the response object accordingly
#     try:
#         response["transcription"] = recognizer.recognize_google(audio)
#     except sr.RequestError:
#         # API was unreachable or unresponsive
#         response["success"] = False
#         response["error"] = "API unavailable"
#     except sr.UnknownValueError:
#         # speech was unintelligible
#         response["error"] = "Unable to recognize speech"
#
#     return response
#
#
# if __name__ == "__main__":
#     # set the list of words, maxnumber of guesses, and prompt limit
#     WORDS = ["apple", "banana", "grape", "orange", "mango", "lemon"]
#     NUM_GUESSES = 3
#     PROMPT_LIMIT = 5
#
#     # create recognizer and mic instances
#     recognizer = sr.Recognizer()
#     microphone = sr.Microphone()
#
#     # get a random word from the list
#     word = random.choice(WORDS)
#
#     # format the instructions string
#     instructions = (
#         "I'm thinking of one of these words:\n"
#         "{words}\n"
#         "You have {n} tries to guess which one.\n"
#     ).format(words=', '.join(WORDS), n=NUM_GUESSES)
#
#     # show instructions and wait 3 seconds before starting the game
#     print(instructions)
#     time.sleep(3)
#
#     for i in range(NUM_GUESSES):
#         # get the guess from the user
#         # if a transcription is returned, break out of the loop and
#         #     continue
#         # if no transcription returned and API request failed, break
#         #     loop and continue
#         # if API request succeeded but no transcription was returned,
#         #     re-prompt the user to say their guess again. Do this up
#         #     to PROMPT_LIMIT times
#         for j in range(PROMPT_LIMIT):
#             print('Guess {}. Speak!'.format(i + 1))
#             guess = recognize_speech_from_mic(recognizer, microphone)
#             if guess["transcription"]:
#                 break
#             if not guess["success"]:
#                 break
#             print("I didn't catch that. What did you say?\n")
#
#         # if there was an error, stop the game
#         if guess["error"]:
#             print("ERROR: {}".format(guess["error"]))
#             break
#
#         # show the user the transcription
#         print("You said: {}".format(guess["transcription"]))
#
#         # determine if guess is correct and if any attempts remain
#         guess_is_correct = guess["transcription"].lower() == word.lower()
#         user_has_more_attempts = i < NUM_GUESSES - 1
#
#         # determine if the user has won the game
#         # if not, repeat the loop if user has more attempts
#         # if no attempts left, the user loses the game
#         if guess_is_correct:
#             print("Correct! You win!".format(word))
#             break
#         elif user_has_more_attempts:
#             print("Incorrect. Try again.\n")
#         else:
#             print("Sorry, you lose!\nI was thinking of '{}'.".format(word))
#             break
# import math
# import os
# import random
# import re
# import sys

# if __name__ == '__main__':
#      a =int(input())  `
#      b=int(input())
#      print(a)
#      print(b)
# n = int(input().strip())
# if n % 2 != 0:
#     print("Weird")
# elif n % 2 == 0:
#     if 2 < n < 5:
#         print('Not Weird')
#     elif 6 < n <=20:
#         print("Weird")
#     #     elif n > 20:
#     #         print("Not Weird")
# def is_leap(year):
#     # Write your logic here
#     if ((year/4 or year/400) and year % 100 == 0):
#         leap = True
#     else:
#         leap = False
#
#     return leap
#
#
# year = int(input())
# print(is_leap(year))n = int(input())
# if __name__ == '__main__':
#     list1=[]
#     list2 =[]
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         list1.append(name)
#         list2.append(score)
#     minimun =min(list2)
#     print(minimun)
#     print(len(list2))
#     fun = []
#     for i in range(len(list2)):
#         if list2[i]==min(list2):
#             list2.remove(list2[i])
#             list1.remove(list1[i])
#     for i in range(len(list2)+1):
#         min2 = min(list2)
#         if list2[i]==min2:
#             print(list1[i])





#
# from itertools import groupby
# print(*[(len(list(g)), int(k)) for k, g in groupby(input())])
#
# # *-> [1,2,3,4]--> 1 2 3 4
# #  k in grouopby -> aabbbccddaaadd = a b c d a d
# # g -> aaaa  bbb cc dd aaa dd



# limit for float
# "{:.2f}".format(a_float)


import os
import pyttsx3
import datetime
import time
import speech_recognition as sr
import wikipedia
import webbrowser
import random

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis , created by Taaaaannnnnnnyyyyyyaaaaaaa Mam")


def takeCommand():
    """for pip error of speechRecognition in Pyaudio problem use this {1)pip install pipwin
    2)pipwin install pyaudio} """
    r = sr.Recognizer()
    time.sleep(3)
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
        try:
            print("Recognizing.......")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
        except Exception as e:
            print("I can't recongnize it , say again")
            return "None"
    return query
    # print(sr.__version__) # just to print the version not required
    # r = sr.Recognizer()
    # my_mic = sr.Microphone() #my device index is 1, you have to put your device index
    # with my_mic as source:
    #     print("Say now!!!!")
    #     audio = r.listen(source) #take voice input from the microphone
    #     response = {
    #     "success": True,
    #     "error": None,
    #     "transcription": None
    #     }
    #     try:
    #         response["transcription"] = r.recognize_google(audio)
    #     except sr.RequestError:
    #     # API was unreachable or unresponsive
    #         response["success"] = False
    #         response["error"] = "API unavailable"
    #     except sr.UnknownValueError:
    #     # speech was unintelligible
    #         response["error"] = "Unable to recognize speech"

    # return response
    # to print voice into text


if __name__ == "__main__":
    # speak("Not a problem speak yourself and write code")
    # wishMe()
    while True:
        query = takeCommand().lower()

        # logic for executing query tasks
        # In Wikipedia
        if 'wikipedia' in query:
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'youtube' in query:
            webbrowser.open('youtube.com')

        elif 'play music' or 'play songs' in query:
            music_dir = 'D:\\SongsPlay\\animeSongs'
            songs = os.listdir(music_dir)
            print(songs)
            length = len(songs)
            take = random.randrange(0, length)
            os.startfile(os.path.join(music_dir, songs[take]))


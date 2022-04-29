import pyttsx3
import datetime
import speech_recognition as sr

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
    # r =sr.Recognizer()
    # with sr.Microphone() as source:
    #     print("Listening.....")
    #     r.pause_threshold = 1
    #     r.energy_threshold =200
    #     audio = r.listen(source)
    print(sr.__version__)  # just to print the version not required
    r = sr.Recognizer()
    my_mic = sr.Microphone()  # my device index is 1, you have to put your device index
    with my_mic as source:
        print("Say now!!!!")
        audio = r.listen(source)  # take voice input from the microphone
        response = {
            "success": True,
            "error": None,
            "transcription": None
        }
        try:
            response["transcription"] = r.recognize_google(audio)
        except sr.RequestError:
            # API was unreachable or unresponsive
            response["success"] = False
            response["error"] = "API unavailable"
        except sr.UnknownValueError:
            # speech was unintelligible
            response["error"] = "Unable to recognize speech"

        return response
    # to print voice into text

    # try:
    #     print("Recognizing.......")
    #     query = r.recognize_google(audio ,language='en-in')
    #     print(f"User said: {query}")
    # except Exception as e:
    #     speak("I can't recongnize it , say again")
    #     return "None"
    # return query


if __name__ == "__main__":
    # speak("Not a problem speak yourself and write code")
    # wishMe()
    takeCommand()
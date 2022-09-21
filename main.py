import sys
import webbrowser
import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listener = sr.Recognizer()
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)


def talk(text):
    alexa.say(text)
    alexa.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk("Good Morning!")

    elif hour >= 12 and hour < 18:
        talk("Good Afternoon!")

    else:
        talk("Good Evening!")
    talk("I am alexa, Please tell me how may I help you")

def take_command():
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source, phrase_time_limit=5)
        listener.pause_threshold=1
    try:
        print("Recognizing...")
        command = listener.recognize_google(voice, language='en-pk')
        command = command.lower()
        print(f"User said: {command}\n")
        if 'alexa' in command:
            command = command.replace('alexa', '')
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return command

def run_alexa():
    command = take_command()
    if 'what the time now' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
        look_for = command.replace('tell me about', '')
        info = wikipedia.summary(look_for, 2)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'love' in command:
        talk('Sorry vaiya, I am in another relation')
    elif 'how old' in command:
        talk('Sorry dear, I am virtual assistant, so I am evergreen')
    elif 'open google' in command:
        webbrowser.open("google.com")
    elif 'who made you' in command:
        talk('Yes sure I am alexa made by Md Torikul Islam,ID 19002131 department  CSE, Green University of Bangladesh')
    elif 'no thank you' in command:
        talk('Good Bye, have a good day.')
        sys.exit()
    else:
        talk('I did not get it but I am going to search it for you')
        pywhatkit.search(command)

while True:
    wishMe()
    run_alexa()
import pyttsx3 as p
import speech_recognition as sr
from selenium_web import infow
from youtube_automation import video
from news import *
import pyjokes
from weather import *
import datetime
import warnings
import wikipedia
import calendar
import webbrowser
import os
from sys import platform
import sys
from diction import translate
import psutil
import pyautogui
from return_xPath import returnXPath

# Setting default values and initialising voice engine
engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 130)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Ignore any warning messages
warnings.filterwarnings('ignore')


# COLOUR PRINTING FUNCTION
def outer_func(colour):
    def inner_function(msg):
        print(f'{colour}{msg}')

    return inner_function


# COLOUR PRINTS
GREEN = outer_func('\033[92m')
YELLOW = outer_func('\033[93m')
RED = outer_func('\033[91m')
BLUE = outer_func('\033[94m')


# BANNER
def banner():
    YELLOW(r'''    
  _
 | |
 | |___       
 |  _  \   _   _
 | |_)  | | (_) |
  \____/   \__, |
            __/ | 
           |___/
                        _                                                         _
                       | |                                                       (_)
  ____     ____     ___| |   ___ _   ______   ______    ___ _   ______   ______   _   _ ____
 / ___\   /    \   /  _  |  / _ | | / _____| / _____|  / _ | | / _____| / _____| | | | |   | \
| |____  |  ()  | |  (_| | | (_|| | \______\ \______\ | (_|| | \______\ \______\ | | | |   | |
 \____/   \____/   \____/   \___|_| |______/ |______/  \___|_| |______/ |______/ |_| |_|   |_|
  ''')


# Record audio and return it as string
def recordAudio():
    # Record the audio
    r = sr.Recognizer()

    # Open the microphone to start recording
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print('listening...')
        audio = r.listen(source)

    # Use Google speech recognition
    data = ''
    try:
        data = r.recognize_google(audio, language='en-in')
        print('You said: ' + data)
    except sr.UnknownValueError:  # Check for unknown errors
        print('Google Speech Recognition could not understand the audio, unknown error')
    except sr.RequestError as e:
        print('Request results from Google Speech Recognition service error ' + e)

    return data


# A function for computer to speak with
def speak(query):
    engine.say(query)
    engine.runAndWait()


# A function for wake word(s) or phrase
def wakeWord(text1):
    WAKE_WORDS = ['hey computer', 'ok computer']

    text1 = text1.lower()
    if text1 in WAKE_WORDS:
        return True
    else:
        return False


# A function to wish the user as per time
def wishMe():
    hour = int(today_date.hour)
    if 0 <= hour < 12:
        response = "Good morning SIR."
    elif 12 <= hour < 18:
        response = "Good afternoon SIR."

    else:
        response = "Good evening SIR."

    return response


# A function to get present date
def getDate():
    present = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = present.month
    dayNum = present.day

    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                   'November', 'December']

    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th',
                      '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th',
                      '26th', '27th', '28th', '29th', '30th', '31st']

    print("Today is " + weekday + " " + month_names[monthNum - 1] + " the " + ordinalNumbers[dayNum - 1])
    speak("Today is " + weekday + " " + month_names[monthNum - 1] + " the " + ordinalNumbers[dayNum - 1])


# A function to greet the user as he/she starts to interact
def greetings():
    print(wishMe() + " I'm your voice assistant.")
    speak(wishMe() + " I'm your voice assistant.")

    print("Today is " + today_date.strftime("%d") + " of " + today_date.strftime("%B") + ", And its currently " + (
        today_date.strftime("%I:%M:%H")))
    speak("Today is " + today_date.strftime("%d") + " of " + today_date.strftime("%B") + ", And its currently " + (
        today_date.strftime("%I:%M:%H")))

    weather()

    print("How are you?")
    speak("How are you?")

    reply = recordAudio()

    if "what" and "about" and "you" in reply:
        print("I am having a good day sir")
        speak("I am having a good day sir")


# A function to separate person name from rest of the sentence
def getPerson(phrase):
    wordlist = phrase.split()

    for i in range(0, len(wordlist)):
        if i + 3 <= len(wordlist) - 1 and wordlist[i].lower() == 'who' and wordlist[i + 1].lower() == 'is':
            return wordlist[i + 2] + ' ' + wordlist[i + 3]


# A function to return CPU status
def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage)

    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)


# A function that speaks jokes
def joke():
    for i in range(5):
        speak(pyjokes.get_jokes()[i])


# A function that takes screenshot and saves it
def screenshot():
    img = pyautogui.screenshot()
    img.save('path of folder you want to save/screenshot.png')


if __name__ == '__main__':

    if platform == "linux" or platform == "linux2":
        chrome_path = '/usr/bin/google-chrome'

    elif platform == "darwin":
        chrome_path = "open -a /Applications/Google\\ Chrome.app"

    elif platform == "win32":
        chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    else:
        print('Unsupported OS')
        exit(1)

    today_date = datetime.datetime.now()
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

    banner()
    greetings()

    while True:
        text = recordAudio()

        if wakeWord(text):
            print("What can I do for you?")
            speak("What can I do for you?")

            response = recordAudio()
            response = response.lower()

            if "information" in response:
                print("You need information related to which topic?")
                speak("You need information related to which topic?")

                information = recordAudio()

                print("searching {} in wikipedia...".format(information))
                speak("searching {} in wikipedia".format(information))

                assist = infow()
                assist.get_info(information)
                # read = assist.speakable()
                # print("reading...")
                # print(read)
                # speak(str(read))

            elif "play" and "video" in response:
                print("Which video do you want me to play?")
                speak("Which video do you want me to play?")

                vid = recordAudio()

                print("Playing {} in youtube...".format(vid))
                speak("Playing {} in youtube".format(vid))

                assist = video()
                assist.play(vid)

            elif "read" and "news" in response:
                print("Sure sir, now I'll read news for you.")
                speak("Sure sir, now I'll read news for you.")

                arr = news()
                for i in range(3):
                    print(arr[i])
                    speak(arr[i])

            elif "show" and "news" in response:
                speak('Ofcourse sir..')
                speak_news()
                speak('Do you want to read the full news...')
                test = recordAudio()
                if 'yes' in test:
                    speak('Ok Sir, Opening browser...')
                    webbrowser.open(getNewsUrl())
                    speak('You can now read the full news from this website.')
                else:
                    speak('No Problem Sir')

            elif "sleep" in response:
                sys.exit()

            elif "location" in response:
                speak("What is the location?")
                location = recordAudio()
                url = "https://google.nl/maps/place/" + location + "/&amp;"
                webbrowser.get('chrome').open_new_tab(url)
                speak('Here is the location ' + location)

            elif "date" in response:
                getDate()

            elif "time" in response:
                now = datetime.datetime.now()
                meridiem = ''
                if now.hour >= 12:
                    meridiem = 'pm'
                    hour = now.hour - 12
                else:
                    meridiem = 'am'
                    hour = now.hour

                if now.minute < 10:
                    minute = '0' + str(now.minute)
                else:
                    minute = str(now.minute)

                print("It is" + str(hour) + minute + " " + meridiem)
                speak("It is" + str(hour) + minute + " " + meridiem)

            elif "who is" in response:
                person = getPerson(response)
                wiki = wikipedia.summary(person, sentences=2)
                print(wiki)
                speak(wiki)

            elif "open youtube" in response:
                print("opening youtube...")
                speak("opening youtube")
                webbrowser.get('chrome').open_new_tab('https://youtube.com')

            elif "open google" in response:
                print("opening google.com...")
                speak("opening google.com")
                webbrowser.get('chrome').open_new_tab("google.com")

            elif "open my website" in response:
                webbrowser.open("mad4souvik.ml")
                print("opening your website ...")
                speak("opening your website mad for souvik.ml")

            elif "dictionary" in response:
                speak("What you want to search in your intelligent dictionary?")
                translate(recordAudio())

            elif "search" and "google" in response:
                speak("What do you want to search for?")
                search = recordAudio()
                url = "https://google.com/search?q=" + search
                webbrowser.get('chrome').open_new_tab(url)
                speak('Here is What I found for' + search)

                try:
                    read = returnXPath().returnRead('//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div['
                                                    '1]/div/div/div/span[1]')
                    speak(read)
                except Exception as e:
                    pass

            elif "play" and "music" in response:
                music_dir = "C:\\Users\\user\\Music\\Video Projects"
                speak("opening music directory for you")
                songs = os.listdir(music_dir)
                speak("printing songs")
                print(songs)
                speak("Playing music...")
                speak("playing music")
                os.startfile(os.path.join(music_dir, songs[0]))

            elif "voice" in response:
                if "female" in response:
                    engine.setProperty("voice", voices[0].id)
                else:
                    engine.setProperty("voice", voices[1].id)
                speak("Hello Sir, I have switched my voice. How is it?")

            elif "cpu" in response:
                cpu()

            elif "joke" in response:
                joke()

            elif "screenshot" in response:
                speak("taking screenshot")
                screenshot()

            elif "sleep" in response:
                sys.exit()

            elif "remember that" in response:
                speak("what should i remember sir")
                rememberMessage = recordAudio()
                speak("you said me to remember" + rememberMessage)
                remember = open('data.txt', 'w')
                remember.write(rememberMessage)
                remember.close()

            elif "do you remember anything" in response:
                remember = open('data.txt', 'r')
                speak("you said me to remember that" + remember.read())

            elif "github" in response:
                webbrowser.get('chrome').open_new_tab('https://github.com/codassassin')

            elif "shutdown" in response:
                if platform == "win32":
                    os.system('shutdown /p /f')
                elif platform == "linux" or platform == "linux2" or "darwin":
                    os.system('poweroff')

            elif "jarvis are you there" in response:
                speak("Yes Sir, at your service")

            elif "open code" in response:
                codePath = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                speak('opening VS CODE')
                os.startfile(codePath)

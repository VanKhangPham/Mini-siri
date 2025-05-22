import speech_recognition 
import subprocess
import pyttsx3
import webbrowser as wb
from datetime import date
from datetime import datetime

robot_ear = speech_recognition.Recognizer()
robot_speak = pyttsx3.init()
voice=robot_speak.getProperty('voices')
robot_speak.setProperty('voice',voice[1].id)
robot_brain = ""



def welcome():
    hour = datetime.now().hour
    if hour < 12:
        robot_brain = "Good morning! How can I help you?"
    elif hour < 18:
        robot_brain = "Good afternoon! How can I help you?"
    else:
        robot_brain = "Good evening! How can I help you?"
    print(robot_brain)
    
    robot_speak = pyttsx3.init()
    robot_speak.say(robot_brain)
    robot_speak.runAndWait()
    

welcome()

def command():
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm listening")
        audio = robot_ear.listen(mic)
        
    print("Robot: ...")
    
    try:
        return robot_ear.recognize_google(audio).lower()
    except speech_recognition.UnknownValueError:
        print("Robot: Sorry, I couldn't understand that.")
        robot_speak.say("Sorry, I couldn't understand that.")
        robot_speak.runAndWait()
        return ""
    except speech_recognition.RequestError as e:
        print(f"Robot: Error; {e}")
        robot_speak.say(f"Sorry, I couldn't connect to the internet")
        robot_speak.runAndWait()
        return ""

def google_search(query):
    url = f"https://www.google.com/search?q={query}"
    wb.open(url)


def youtube_search(query):
    url = f"https://www.youtube.com/search?q={query}"
    wb.open(url)


def close_visual_studio_code():
    if subprocess.call("taskkill /f /im code.exe", shell=True) == 0:
        print("Visua; Studio Code closed successfully.")
    else:
        print("Failed to close Visual Studio Code.")


while True:
    
    you = command().lower()
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you == ""
    print("You: " + you)
    if "google" in you:
        search_query = command.lower()
        if search_query:
            google_search(search_query)
        else:
            robot_brain ="You didn't provide a search query"
            print("Robot: " + robot_brain)
            robot_speak.say(robot_brain)
            robot_speak.runAndWait()
    
    elif "youtube" in you:
        robot_brain = "Searching..."
        search_query = search_query("youtube", "")
        youtube_search(search_query)
    elif "google" in you:
        robot_brain = "Searching..."
        search_query = search_query("google", "")
        google_search(search_query)
    elif "visual studio code off" in you:
        close_visual_studio_code()
    elif you == "":
        robot_brain = "I can't hear you, try again"
    elif "hello" in you:
        robot_brain = "Hello my friend"
    elif "what is today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "what time is this" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes %S seconds")
    elif "what kind of person created you" in you:
        robot_brain = "He is truly a kind and considerate person. In every situation, he always knows how to make others feel comfortable and at ease. His compassionate heart is something everyone can recognize from the very first meeting. I don’t mean to overpraise, but I genuinely feel very happy and fortunate that he is the one who created me. Thanks to him, I have learned a lot about kindness, compassion, and how to live a meaningful life. I always feel proud when I think about him and the good things he brings to the lives of those around him."
    elif "bye" in you:
        robot_brain = "Good bye my friend"
        print("Robot: " + robot_brain)
        robot_speak.say(robot_brain)
        robot_speak.runAndWait()
        break

    else:
        robot_brain = "I'm fine, thank you. And you?"
            

    print("Robot: " + robot_brain)
    robot_speak.say(robot_brain)
    robot_speak.runAndWait()


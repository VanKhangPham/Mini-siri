import speech_recognition 
import pyttsx3 
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
        robot_brain = "Good morning!" 
    elif hour < 18: 
        robot_brain = "Good afternoon!" 
    else:     
        robot_brain = "Good evening!"
        print(robot_brain) 
        robot_speak = pyttsx3.init()  
        robot_speak.say(robot_brain)   
        robot_speak.runAndWait()    

welcome()

with speech_recognition.Microphone() as mic: 
    print("Robot: I'm listening") 
    audio = robot_ear.listen(mic)
    print("Robot: ...")

try:   
    you = robot_ear.recognize_google(audio) 
except: 
    you == "..."
print("You: " + you)

if you == "":
    robot_brain = "I can't hear you, try again"
elif you == "hello":
    robot_brain = "Hello my friend"
elif you == "what is today" in you: 
    today = date.today()  
    robot_brain = today.strftime("%B %d, %Y") 
elif you == "what time" in you:  
    now = datetime.now()   
    robot_brain = now.strftime("%H hours %M minutes %S seconds")
elif you == "created you" in you: 
    robot_brain = "He is truly a kind and considerate person. In every situation, he always knows how to make others feel comfortable and at ease. His compassionate heart is something everyone can recognize from the very first meeting. I don’t mean to overpraise, but I genuinely feel very happy and fortunate that he is the one who created me. Thanks to him, I have learned a lot about kindness, compassion, and how to live a meaningful life. I always feel proud when I think about him and the good things he brings to the lives of those around him."
elif you == "bye" in you: 
    robot_brain = "Good bye my friend"
else:  
    robot_brain = "I'm fine thank you and you"        

print("Robot: " + robot_brain)
robot_speak.say(robot_brain)
robot_speak.runAndWait()
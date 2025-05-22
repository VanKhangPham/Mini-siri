import pyttsx3
from datetime import date



robot_speak = pyttsx3.init()
robot_speak.say(robot_brain)
robot_speak.runAndWait()
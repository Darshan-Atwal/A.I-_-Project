import time
import webbrowser as wb
import speech_recognition as sr
import os
import pyautogui as pg
import datetime
import pyttsx3
engine=pyttsx3.init()
#code
def say(name):
    engine.say(name)
    engine.runAndWait()
__timenow__=datetime.datetime.now().hour
__clientname__=pg.prompt(text="Please enter your name", title='Client Information')
__clientgender__=pg.prompt(text="Please enter your Gender", title='Client Information')

if __clientgender__=='male' or __clientgender__=='Male' or __clientgender__=='female' or __clientgender__=='Female':
    pass
else:
    time.sleep(0.9)
    print('Unknown Gender, Gender authentification failed.')
    say('Unknow. gender, Gender authentification failed')
os.system('clear')
time.sleep(0.9)
print("initialising....")
time.sleep(0.9)
if __timenow__>=12 and __timenow__<=16:
    print("Good Afternoon "+__clientname__+"!")
    say("Good Afternoon "+__clientname__+"!")
elif __timenow__>16 and __timenow__<24:
    print('Good evening '+__clientname__+"!")
    say('Good evening '+__clientname__+'!')
elif __timenow__>=0 and __timenow__<12:
    print('Good morning '+__clientname__+'!')
    say('Good morning '+__clientname__+'!')
print('I am your health care assistant!')
say('i am your health care assistant')
print('My name is Jack')
say('my name is jack!')
def takecommand():
    try:
        r=sr.Recognizer()
        with sr.Microphone() as Source:
            print('Listninig...')
    except ModuleNotFoundError as e:
        print(e)
    except AttributeError as ae:
        print(ae)
takecommand()

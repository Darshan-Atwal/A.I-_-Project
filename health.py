import time
import webbrowser as wb
import pywhatkit as pwt
import speech_recognition as sr
import os
import wikipedia as googlescrap
import pyautogui as pg
import datetime
import pyttsx3
engine=pyttsx3.init()
#code
def say(name):
    print(name)
    engine.say(name)
    engine.runAndWait()
__timenow__=datetime.datetime.now().hour
__clientname__=pg.prompt(text="Please enter your name", title='Client Information')
__clientgender__=pg.prompt(text="Please enter your Gender", title='Client Information')
if __clientgender__=='male' or __clientgender__=='Male' or __clientgender__=='female' or __clientgender__=='Female':
    pass
else:
    time.sleep(0.9)
    say('Unknow. gender. Gender authentification failed')
os.system('clear')
time.sleep(0.9)
print("initialising....")
time.sleep(0.9)
if __timenow__>=12 and __timenow__<=16:
    say("Good Afternoon "+__clientname__+"!")
elif __timenow__>16 and __timenow__<24:
    say('Good evening '+__clientname__+'!')
elif __timenow__>=0 and __timenow__<12:
    say('Good morning '+__clientname__+'!')
time.sleep(0.5)

say('i am your health care assistant')
time.sleep(0.5)

say('my name is jack!')
#trial change
def takecommand():
    try:
        r=sr.Recognizer()
        with sr.Microphone() as Source:
            print('Listninig...')
    except ModuleNotFoundError as e:
        print(e)
    except AttributeError as ae:
        print(ae)
print('How can i help you?\n: ')
while True:
    inp=input('--> ')
    if inp=='search':
        print('what do you want to search: ')
        inps=input('--> ')
        time.sleep(0.9)
        say("This is what i found on the web!")
        try:
            pwt.search(inps)
            result=googlescrap.summary(inps,3)
            say(result)
        except Exception as e:
            say('Cant Call the Data')   

        

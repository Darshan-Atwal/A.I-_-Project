import time
import webbrowser as wb
try:
    import pywhatkit as pwt
except Exception as e:
    print('cant connect to the internet')
    print(f'Please check your internet connection')
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
__clientLoaction__=pg.prompt(text="Please enter your city", title='Client Information')
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
try:
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
        elif inp=='quit':
            say("Thanks for using my project!")
            break
        elif inp=='Indian healthcare website':
            try:
                say('This is your result')
                wb.open_new_tab('https://www.mohfw.gov.in/')
            except Exception as e:
                say('oops, Unable to fetch data at this moment!')
        elif inp=='cure for disease':
            print('For which disease do you want cure?')
            inps=input('--> ')
            try:
                pwt.search('cure for '+inps)
                result=googlescrap.summary()
                say(result)
            except Exception as e:
                print('Unable to fetch callable data at this moment!')
        elif inp=="Hospitals near me":
            try:
                pwt.search('Hospitals near '+__clientLoaction__)
            except Exception as e:
                print(e)
        elif inp=='Diagnose a disease':
            say('Please wait till i fetch the best site for you.')
            time.sleep(1)
            wb.open_new_tab('https://symptomate.com/diagnosis/0')
        elif inp=='ai -help':
            print('Type "search" to search on google')
            print('Type "cure for disease" to find an cure')
            print('Type "Indian healthcare website" for accessing the indian healthcare website')
            print('Type "Hospitals near me" to see the nearest hospitals ')
            print('Type "quit" to quit')

        else:
            print('oops, i am not able to fetch that at this moment! type ai -help for more')
except Exception as e:
    print('Please check your internet connection')            

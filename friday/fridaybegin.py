import os
import sys
import speakthis
import malespeaker
import json
import time
import gui
import transcribe
import random
import pyautogui
import apimain
import online


def main():
    message = ["anything else sir","what else can i do for you","can i be of any further assistant"]
    
    os.startfile("C://Users//Envy15//Desktop//friday//abc.bat")
    time.sleep(2)
    pyautogui.click(100, 100);
    pyautogui.click(100, 100);
    malespeaker.speak("Hello Sir... I am Your personal voice controlled assistant....Following are my functionalities which I support")
    s = "I can fetch your mails"+"\nGoogle search anything"+"\nI can get news updates"+"\nI can get you dates, time, calendar"
   # s+="I can can open your favourite folder"+"\nI can play music"+"\nI can calculate maths expressions"+"\nI can give you weather report of any location"+"\nI can shutdown, restart, sign out this device"
   # s+="\nI can open taskmanager or settings of this device"+"\nI can scrollup scrolldown and increase decrease volume of device"+"\nI can take snapshot for you"+"\nI can open command prompt if you want"+"\nI can write a note for you"+"\nI can set a reminder"+"\nI can set an alarm"+"\nI can get you connected to your social media"+"\nI can work as dictionary for you"
    malespeaker.speak(s)
    malespeaker.speak("How can I help You?")
        
    #malespeaker.speak(s)
    x=1
    while x!=0:
        print()
        print("Your query")
        query = transcribe.transcribe_file()
        #query = input()
        #query = '@'+query
        #if query[0] is '#':
        #    online.need(query)

        #elif query[0] is '@':
        
        apimain.get(query)

        time.sleep(3)
        #malespeaker.speak(message[0])
        #opt = transcribe.transcribe_file()
        #opt = input("Your option sir : ")
        #if "no" in opt:
        #    x=0
        #else:
        #malespeaker.speak("Please say your query")


if __name__ == '__main__':
    main()

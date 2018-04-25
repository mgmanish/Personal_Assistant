import os 
import sys
import malespeaker
def exec(q):
    if("close yourself" in q or "exit" in q or "close urself" in q):
        malespeaker.speak("closing myself sir")
        os.system("close /p")

    elif("none" in q):
        print("hello")


        
if __name__ == '__main__':
    exec("close")

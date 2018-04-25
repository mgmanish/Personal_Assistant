import time
import malespeaker
def fun():
        malespeaker.speak("Wait while we retrieve your twitter feed ")
        time.sleep(10)
        s = "cristiano ronaldo tweeted una victoria importante en paris, wamos equipo"
        print(s)
        print()
        malespeaker.speak(s)
        s= "Elon musk tweeted i just realized there is a jazz hands emoji"
        print(s)
        print()
        malespeaker.speak(s)
        s = "bill gates tweeted most people know @rogerfederer as one of the greatest tennis  player of all time but his work off the court is also impressive"
        print(s)
        print()
        malespeaker.speak(s)
        s = "coindesk tweeted ex-imf economist bitcoin could drop to $100 in next decade"
        print(s)
        print()
        malespeaker.speak(s)
        s= "nasa tweeted what a view before its graceful farewell @cassinisaturn"
        print(s)
        print()
        malespeaker.speak(s)
        return s

if __name__ == '__main__':
        fun()

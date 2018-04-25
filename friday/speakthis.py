from gtts import gTTS
import time
import os
def speak(x):
    tts = gTTS(text=x, lang='en')
    tts.save("good.mp3")
    os.system("good.mp3")

if __name__ == '__main__':
    speak("python ")




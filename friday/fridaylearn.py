import malespeaker
import transcribe

def fun(q):
	s ="Okay Sir Just tell me answer your query and i will learn it for next time"
	print(s)
	malespeaker.speak(s)
	ans = input()
	s = q+":"+ans
	f = open("14.txt",'a')
	f.write(s)

if __name__ == "__main__":
	fun("who is my best friend")
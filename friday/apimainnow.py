import os
import time
import news
import quickstart
import malespeaker
import transcribe
import calendar
import datetime
import subprocess
import re
import search
import fbnot
import mntwt
import gui
import requests
import takenote
import getpass
import pyautogui
import datame
import captureimage
import mntwt
import windowcommand
import close
import weatherupdates
import fridaylearn
def remove(s):
	return ''.join(['' if ord(i) < 123 and ord(i)>96 else i for i in s])
def get(q):
	q = q.lower()
	fileno=0
	name = {1:["weather","climate","temperature","forecast"],2:["news","recent stories","information","trending updates"],3:["mail","mails","gmail","email"],4:["calendar","schedule","timetable"],5:["date","time"],6:["snapshot","screenshot","selfie"],
	7:["write","notedown","compose","autograph","printout"],8:["twitter","tweets"],9:["shutdown","finish"],10:["music","song","songs","playlist","collection","collections"],
	11:["folder","file","favourite folder"],12:["task manager","working applications"],13:["control panel","settings"],25:["teach","learn","train","remember"]}
	print(name[1])
	for i in range(1,15):
		x=1
		s = str(i)
		s+=".txt"
		#print(s)
		f = open(s,'r')
		lines = f.readlines()
		f.close()
		for line in lines:
			if q in line or line in q:
				print("hey we have found file you are talking about")
				print(name[i])
				x=0
				fileno = i
			if x == 0:
				break
			if x == 1:
				print("We could not understand your query sir")
				print("Please tell me to which feature your query is related to")
				ans = input()
				for i in range(1,15):
					for namee in name[i]:
						if namee in ans:
							print(namee)
							s = str(i)+".txt"
							#print(s)
							fileno=i
							f = open(s,'r')
							lines = f.readlines()
							f.close()
							stri=""
							for line in lines:
								stri = stri+line
								stri = stri+"\n"
								stri = stri+q
								f = open(s,'w')
								f.write(stri)
								f.close()
								break
								if fileno == i:
									break
									print(fileno)
									if fileno==1:
										weatherupdates.fun(q)
									elif fileno==2:
										news.allnews()
									elif fileno==3:
										quickstart.mails()
									elif fileno==4:
										c = calendar.TextCalendar(calendar.SUNDAY)
										if("next month" in q):
											strx = c.formatmonth(2017+int((datetime.datetime.now().month+1)/12),((datetime.datetime.now().month+1)%12))
										elif("previous month" in q):
											strx = c.formatmonth((2017-int((datetime.datetime.now().month-1)/12)),(datetime.datetime.now().month-1)%12)
										else:
											strx = c.formatmonth(2017,datetime.datetime.now().month)
											gui.fun(strx)
											return
									elif fileno==5:
										datame.fun()
									elif fileno==6:
										captureimage.fun()
									elif fileno==7:
										takenote.notedown(q)
									elif fileno==8:
										mntwt.fun()
									elif fileno==9:
										windowcommand.exec(q)
									elif fileno==10:
										os.system('E:\\songs\\oldcollections\\1.mp3')
									elif fileno==11:
										subprocess.call("explorer F:\\Movies", shell=True)
									elif fileno==12:
										subprocess.Popen("C:\Windows\System32\\Taskmgr.exe", shell=True)
									elif fileno==13:
										subprocess.Popen("C:\Windows\System32\\control.exe", shell=True)
									elif fileno==14:
										f = open("14.txt",'r')
										lines = f.readlines()
										for line in lines:
											if q in line:
												s = q+":"
												line.replace(s,"")
												print(line)
									elif fileno==25:
										fridaylearn.fun(q)






if __name__ == '__main__':
	get(" weather forecast in new york ")
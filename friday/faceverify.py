import os
import captureimage
import malespeaker
import detectface
import verifycall
def fun():
	x=1
	k=1
	new=""
	while x != 2:
		p = captureimage.fun()
		os.system("a.bat")
		k += 1
		x=2
		try:
			new = detectface.fun("https://rawgit.com/vikas12396/axis123/master/"+str(p)+'.jpg')
		except:
			malespeaker.speak("Sorry Sir Your Image was not clear... My advice is to come closer to camera or in some light also..")
			if k<4:
				x=1
			else:
				return "yes"

	admin = detectface.fun("https://rawgit.com/vikas12396/axis123/master/gp.png")
	print(new)
	print(admin)
	result = verifycall.test_verify(new,admin)
	print(result)
	if result:
		return "yes"
	else:
		return "no"

if __name__ == '__main__':
	fun()
from cv2 import *
import time
import random
# initialize the camera
def fun():
    cam = VideoCapture(0)   # 0 -> index of camera	
    s, img = cam.read()
    cam.release()
    if s:    # frame captured without any errors
        namedWindow("cam-test",1280)
        imshow("cam-test",img)
        waitKey(500)
        destroyWindow("cam-test")
        p = random.randint(1,10001)
        x = 'C:/users/rpsvi/python-getting-started/'+str(p)+'.jpg'
        imwrite(x,img)
        return p

if __name__ == '__main__':
	fun()

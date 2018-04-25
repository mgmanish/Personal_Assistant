import os
import pyautogui
from os import path

def main():
    pyautogui.hotkey('win','s')
    if path.exists("guru99.txt"):
	# get the path to the file in the current directory
        src = path.realpath("guru99.txt");
		
	# rename the original file
        os.rename("career.guru99.txt","guru99.txt")
		
if __name__ == "__main__":
    main()

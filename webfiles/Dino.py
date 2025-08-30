import pyautogui
from PIL import ImageGrab
import time

def hit(key):
    pyautogui.keyDown(key)

def takeScreenshot():
    return ImageGrab.grab().convert("L")  

if __name__ == "__main__":
    time.sleep(1)
    image = takeScreenshot()
    data = image.load()
    for i in range(320, 380):
        for j in range(300, 355):
            data[i, j] = 0

    image.show()  


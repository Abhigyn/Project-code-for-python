import pyautogui
from PIL import ImageGrab
import time
pyautogui.FAILSAFE = False
def hit(key):
    pyautogui.press(key)

def isColide(data):
        # for birds    
    for i in range(370, 400):
        for j in range(200, 310):
         if data[i, j] <100:
            hit("down") 
# for catus
        for i in range(370, 400):
            for j in range(300, 320):
                if data[i, j] <100:
                     hit("up")
if __name__ == "__main__":
    print("hey.. dino game is about to start in 3 second")
    time.sleep(3)
    # hit("up")
    while True:
        image = ImageGrab.grab().convert("L")
        data = image.load()
        # isColide(data)

        for i in range(390, 450):
             for j in range(300, 320):
                 data[i, j] = 171

                 for i in range(390, 400):
                     for j in range(200, 310):
                         data[i, j] = 0
        image.show()
        break     
        



import pyautogui
import cv2
import numpy as np
from PIL import ImageGrab
import time

pyautogui.FAILSAFE = False

def hit(key):
    pyautogui.press(key)

def isColide(gray):
    # Bird zone
    bird_zone = gray[200:310, 420:460]   # slice out region
    if (bird_zone < 100).any():
        hit("down")
        return

    # Cactus zone
    cactus_zone = gray[280:320, 420:473]
    if (cactus_zone < 100).any():
        hit("up")
        return

if __name__ == "__main__":
    print("hey.. dino game is about to start in 3 seconds")
    time.sleep(3)
    hit("up")

    while True:
        # grab screenshot
        img = np.array(ImageGrab.grab())
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # check collision
        isColide(gray)

        # draw debug rectangles
        cv2.rectangle(img, (420, 200), (460, 310), (0, 0, 255), 2)  # red bird zone
        cv2.rectangle(img, (420, 280), (473, 320), (255, 0, 0), 2)  # blue cactus zone

        # show live debug window
        cv2.imshow("Dino Bot Debug", img)

        # quit with q
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cv2.destroyAllWindows()

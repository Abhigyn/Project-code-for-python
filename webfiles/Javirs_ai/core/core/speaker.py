from gtts import gTTS
import pygame
import os

def speak(text):
    print("JARVIS:", text)
    tts = gTTS(text)
    tts.save("temp.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pass
    pygame.mixer.quit()
    os.remove("temp.mp3")

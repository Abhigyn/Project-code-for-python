import speech_recognition as sr

recognizer = sr.Recognizer()

def listen_for_jarvis():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening for 'Jarvis'...")
        try:
            audio = recognizer.listen(source, timeout=4)
            word = recognizer.recognize_google(audio)
            if "jarvis" in word.lower():
                print("Activated. Listening for command...")
                speak("Yes?")
                audio = recognizer.listen(source, timeout=5)
                command = recognizer.recognize_google(audio)
                return command
        except Exception as e:
            print(f"Error: {e}")
            return None

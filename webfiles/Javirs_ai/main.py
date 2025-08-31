from core.listener import listen_for_jarvis
from core.command_handler import process_command
from core.speaker import speak

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        command = listen_for_jarvis()
        if command:
            process_command(command)

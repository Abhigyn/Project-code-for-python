from core.speaker import speak
from modules import weather, news, wikipedia_search, jokes, translator

def process_command(command):
    command = command.lower()

    if "weather" in command:
        weather.get_weather()
    elif "news" in command:
        news.get_news()
    elif "joke" in command:
        jokes.tell_joke()
    elif "wikipedia" in command:
        wikipedia_search.search(command)
    elif "translate" in command:
        translator.translate(command)
    else:
        from core.nlp import ai_response
        result = ai_response(command)
        speak(result)

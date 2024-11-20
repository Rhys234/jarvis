import openai

from SpeechInputOutput import speak, listen
from DataAnalysis import get_weather
from DeviceIntegration import open_file, play_music


def main():
    speak("Hello, I am JARVIS. How can I assist you?")
    while True:
        command = listen()
        if command:
            if "weather" in command:
                speak("Which city?")
                city = listen()
                if city:
                    weather = get_weather(city)
                    speak(weather)
            elif "open file" in command:
                speak("Please specify the file path.")
                file_path = listen()
                if file_path:
                    response = open_file(file_path)
                    speak(response)
            elif "play music" in command:
                response = play_music()
                speak(response)
            elif "stop" in command:
                speak("Goodbye!")
                break
            else:
                speak("Sorry, I don't understand that command.")

import random
responses = [
    "I'm sorry, Dave. I'm afraid I can't do that.",
    "Of course, sir. Right away.",
    "I live to serve, Tony."
]
def witty_response():
    return random.choice(responses)


openai.api_key = "your_openai_api_key"

def ask_openai(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

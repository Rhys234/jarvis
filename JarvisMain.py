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
